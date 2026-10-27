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
        'properties': {'company': {"type": "string", "description": 'the company the user is searching for'}
        },
        'required': ['company']}
}

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    tools=[get_lead_tool],
    messages=[{"role": "user", "content": "What do we know about google"}]
)
for block in response.content:
    if block.type == "tool_use":
        print(get_lead(block.input['company']))

