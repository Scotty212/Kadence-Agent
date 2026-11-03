leads = [
    {'company': 'google',
    'contact': 'jeff',
    'contact_email': 'jeff@gmail.com',
    'city': 'london',
    'industry': 'tech',
    'mrr': 80000,
    'market_cap': 1000000,
    'company_size': 100},

    {'company': 'tesco',
    'contact': 'mike',
    'contact_email': 'mike@gmail.com',
    'city': 'manchester',
    'industry': 'supermarket',
    'mrr': 50000,
    'market_cap': 3000000,
    'company_size': 70},

    {'company': 'housingco',
    'contact': 'steve',
    'contact_email': 'steve@gmail.com',
    'city': 'leeds',
    'industry': 'construction',
    'mrr': 40000,
    'market_cap': 5000000,
    'company_size': 50},

    {'company': 'dominoes',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'birmingham',
    'industry': 'fast food',
    'mrr': 10000,
    'market_cap': 8000000,
    'company_size': 200},
    
    {'company': 'shein',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'manchester',
    'industry': 'clothing',
    'mrr': 50000,
    'market_cap': 2000000,
    'company_size': 200},

     {'company': 'jd',
    'contact': 'mo',
    'contact_email': 'mo@gmail.com',
    'city': 'birmingham',
    'industry': 'retailer',
    'mrr': 30000,
    'market_cap': 3000000,
    'company_size': 200}   
]

def search_leads(city, industry, min_size, max_size):
    new_leads = []
    for i in leads:
        if i['city'] == city.lower() or i['city'] == None and i['company_size'] >= min_size and i['industry'] == industry.lower() and i['company_size'] <= max_size:
            new_leads.append(i) 
    return (new_leads)
            
def get_lead(company):
    for i in leads:
        if i['company'] == company.lower():
            return i
    return 'Lead not found'



def score_lead(company):
    company_score = []
    
    for lead in leads:
        if lead['company'] == company.lower():
            size_score = lead['company_size'] * 0.10
            mrr_score = lead['mrr'] // 1000
            marketcap_score = lead['market_cap'] // 100000
            score = marketcap_score + mrr_score + size_score

            company_score.append({
                'company': lead['company'],
                'score': score
            })
            return company_score
    return 'lead not found'




