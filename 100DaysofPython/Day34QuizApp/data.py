import requests

params = {
    'amount': 10,
    'type': 'boolean',
}

response = requests.get('https://opentdb.com/api.php', params=params)
response.raise_for_status()
json = response.json()
question_data = json['results']
