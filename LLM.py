from dotenv import load_dotenv
import anthropic
from main import get_lead

load_dotenv()                  
client = anthropic.Anthropic() 

get_lead_tool = {
    'name': 'get_lead',
    'description': 'use this when the user asks for info about the specific company',
    'input_schema': {
        'type': 'object',
        'properties': {
            'company': {
                "type": "string", "description": 'the company the user is searching for'
                }
        },
        'required': ['company']
        }
}

messages = [{"role": "user", "content": "What do we know about google"}]

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    tools=[get_lead_tool],
    messages=messages
)

messages.append({"role": "assistant", "content": response.content})

for block in response.content:
    if block.type == "tool_use":
        result = (get_lead(block.input['company']))
        result = str(result)
        messages.append({"role": "user", "content":[
            {"type": "tool_result", "tool_use_id": block.id, "content": result}
        ]})

final_response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    tools=[get_lead_tool],
    messages=messages
)

for block in final_response.content:
    if block.type == "text":
        print(block.text)
