import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

data = r.json()

print(data)



