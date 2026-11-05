from dotenv import load_dotenv
import anthropic
from main import get_lead
from main import search_leads
from main import score_lead
from main import draft_email

load_dotenv()                  
client = anthropic.Anthropic() 


with open('kadence_prompt.txt', mode='r', encoding='utf-8') as file:
    kadence_info = file.read()


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
         }
        }
}

score_lead_tool = {
    'name': 'score_lead',
    'description': 'use this when user asks for the score of a specific company',
    'input_schema': {
        'type': 'object',
        'properties':{
            'company': {
                'type': 'string', 'description': 'the company the user is searching for'
            }
            },
            'required': ['company']
        }
    }

draft_email_tool = {
    'name': 'draft_email',
    'description': 'use this when user wants to draft an cold email to the lead, you save the email after running',
    'input_schema': {
        'type': 'object',
        'properties': {
            'company': {'type': 'string', 'description': 'the company the user is searching for'},
            'subject': {'type': 'string', 'description': 'the email subject for the draft email'},
            'body': {'type': 'string', 'description': 'the body of the draft email'}
        },
        'required': ['company', 'subject', 'body']
    }
}

messages = [{'role': 'user', 'content': 'draft an email to tesco explaining what kadence does and how we can help'}]

response = client.messages.create(
    model='claude-haiku-5-5',
    max_tokens=10000,
    tools=[get_lead_tool, search_leads_tool, score_lead_tool, draft_email_tool],
    messages=messages,
    system=kadence_info
)

while response.stop_reason == 'tool_use':
    messages.append({'role': 'assistant', 'content': response.content})
    for block in response.content:
        if block.type == 'tool_use':
            if block.name == 'get_lead':
                result = (get_lead(block.input['company']))  
                result = str(result)      
            if block.name == 'search_leads':
                result = (search_leads(block.input.get('city'), block.input.get('industry'), block.input.get('min_size', 1), block.input.get('max_size',20000)))
                result = str(result)
            if block.name == 'score_lead':
                result = (score_lead(block.input.get('company')))
                result = str(result)
            if block.name == ('draft_email'):
                result = (draft_email(block.input.get('company'), block.input.get('subject'), block.input.get('body')))
                result = str(result)
            messages.append({'role': 'user', 'content':[{'type': 'tool_result', 'tool_use_id': block.id, 'content': result}]})

    response = client.messages.create(
        model='claude-haiku-5-5',
        max_tokens=10000,
        tools=[get_lead_tool, search_leads_tool, score_lead_tool, draft_email_tool],
        messages=messages,
        system=kadence_info
    )
for block in response.content:
    if block.type == 'text':
        print(block.text)

