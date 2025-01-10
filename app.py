from xml.etree.ElementTree import indent

import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
data_restaurant = {}

try:
    json_file = response.json()
    for item in json_file:
        company = item['Company']

        if company not in data_restaurant:
            data_restaurant[company] = []

        data_restaurant[company].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
except:
    print(response.status_code)

for company, data in data_restaurant.items():
    file_name = f'{company}.json'
    with open(file_name, 'w', encoding='utf-8') as file_restaurant:
        json.dump(data, file_restaurant, ensure_ascii=False, indent=4)