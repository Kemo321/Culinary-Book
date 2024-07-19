import json
import requests


def get_response(query):
    with open('app.json') as f:
        data = json.load(f)
        app_id = data['app_id']
        app_key = data['app_key']
    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}'
    response = requests.get(url).json()
    with open('recipes.json', 'w') as f:
        json.dump(response, f, indent=2)
        print('Recipes loaded!')
