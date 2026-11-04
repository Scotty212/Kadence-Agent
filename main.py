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
    for lead in leads:
        if lead['company'] == company.lower():
            reasons = []

            if lead['market_cap'] <= 10000:
                marketcap_score = 10
                reasons.append('market cap under 10k: small, ideal client')
            elif lead['market_cap'] <= 100000:
                marketcap_score = 8
                reasons.append('market cap 10k-100k: good fit')
            else:
                marketcap_score = 4
                reasons.append('market cap over 100k: may be too big')

            if lead['mrr'] <= 10000:
                mrr_score = 10
                reasons.append('MRR under 10k: likely needs help scaling')
            elif lead['mrr'] <= 100000:
                mrr_score = 8
                reasons.append('MRR 10k-100k: can afford us')
            else:
                mrr_score = 4
                reasons.append('MRR over 100k: may have in-house tools')

            if lead['company_size'] <= 50:
                size_score = 10
                reasons.append('under 50 staff: ideal size')
            elif lead['company_size'] <= 100:
                size_score = 8
                reasons.append('51-100 staff: good size')
            else:
                size_score = 4
                reasons.append('over 100 staff: probably too big')

            total = round((marketcap_score + mrr_score + size_score) / 3, 1)

            return {
                'company': lead['company'],
                'score': total,
                'reasons': reasons
            }

    return 'lead not found'

    
print(score_lead('jd'))



