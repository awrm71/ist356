'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'
'''

import requests

url = "https://cent.ischool-iot.net/api/funnyname/random"
querystring = {"n":"3", 'name':'bob'}
#^ this is different each time
# same in every api
response = requests.get(url, params=querystring)
response.raise_for_status()
names = response.json()
#what comes out is different in every api
for name in names:
    print(name['first'], name['last'])


url = "https://cent.ischool-iot.net/api/funnyname/search"
querystring = {'q':'Mi'}
#^ this is different each time
# same in every api
response = requests.get(url, params=querystring)
response.raise_for_status()
names = response.json()
#what comes out is different in every api
for name in names:
    print(name['first'], name['last'])