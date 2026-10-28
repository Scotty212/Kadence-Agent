from dotenv import load_dotenv
import anthropic
from main import get_lead
from main import search_leads

load_dotenv()                  
client = anthropic.Anthropic() 

get_lead_tool = {
    'name': 'get_lead',
    'description': 'use this when the user asks for info about the specific company',
    'input_schema': {
        'type': 'object',
        'properties': {
            'company': {
                "type": 'string', 'description': 'the company the user is searching for'
                }
        },
        'required': ['company']
        }
}

search_leads_tool = {
    'name': 'search_leads',
    'description': 'use this when the user asks for info about all companies with specific filters',
    'input_schema': {
        'type': 'object',
        'properties': {
            'city': {"type": "string", "description": 'the city the user is searching in'},
            'industry': {'type': "string", "description": 'the industry the user searching for'},
            'min_size':{'type': 'integer', 'description': 'the minimum number of staff in the company the user is searching for, default is 1'},
            'max_size':{'type': 'integer', 'description': 'the maximum number of staff in the company the user is searching for, default is 20,000 '}
        },
        'required': ['city', 'industry', 'min_size', 'max_size']
        }
}

messages = [{'role': 'user', 'content': 'companies in leeds'}]

response = client.messages.create(
    model='claude-haiku-5-5',
    max_tokens=1000,
    tools=[get_lead_tool, search_leads_tool],
    messages=messages
)

messages.append({'role': 'assistant', 'content': response.content})

print(messages)

for block in response.content:
    if block.type == 'tool_use':
        if block.name == 'get_lead':
            result = (get_lead(block.input['company']))  
            result = str(result)      
        elif block.name == 'search_leads':
            result = (search_leads(block.input['city'], block.input['industry'], block.input['min_size'], block.input['max_size']))
            result = str(result)
            print(block.input)
        messages.append({'role': 'user', 'content':[{'type': 'tool_result', 'tool_use_id': block.id, 'content': result}]})


final_response = client.messages.create(
    model='claude-haiku-5-5',
    max_tokens=1000,
    tools=[get_lead_tool, search_leads_tool],
    messages=messages
)

for block in final_response.content:
    if block.type == 'text':
        print(block.text)


