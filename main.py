from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    try:
        json_file = response.json()
        if restaurant is None:
            return {'Dados': json_file}

        data_restaurant = []

        for item in json_file:
            if restaurant == item['Company']:
                data_restaurant.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

        return {'Restaurant': restaurant, 'Menu': data_restaurant}

    except:
        return {'Erro': f'{response.status_code} - {response.text}'}