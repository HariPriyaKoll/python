import requests 
import json

response = requests.get('https://api.zippopotam.us/us/90210')
data = json.loads(response.text)
print(data['country'])
print(data['places'][0]['place name'])
print("print('what ever you want')")