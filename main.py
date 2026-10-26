leads = [
    {'company': 'google',
    'contact': 'jeff',
    'contact_email': 'jeff@gmail.com',
    'city': 'london',
    'industry': 'tech',
    'company_size': 100},

    {'company': 'tesco',
    'contact': 'mike',
    'contact_email': 'mike@gmail.com',
    'city': 'manchester',
    'industry': 'supermarket',
    'company_size': 70},

    {'company': 'housingco',
    'contact': 'steve',
    'contact_email': 'steve@gmail.com',
    'city': 'leeds',
    'industry': 'construction',
    'company_size': 50},

    {'company': 'dominoes',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'birmingham',
    'industry': 'fast food',
    'company_size': 200},
    
    {'company': 'shein',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'manchester',
    'industry': 'clothing',
    'company_size': 200},

     {'company': 'jd',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'birmingham',
    'industry': 'retailer',
    'company_size': 200}   
]

def search_leads(city, industry, min_size, max_size):
    new_leads = []
    for i in leads:
        if i['city'] == city and i['company_size'] >= min_size and i['industry'] == industry and i['company_size'] <= max_size:
            new_leads.append(i) 
    return (new_leads)
            
