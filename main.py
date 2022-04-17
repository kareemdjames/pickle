import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'


def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()


def get_pages(response):
    return response['info']['pages']


def parse_json(response):
    character_list = []
    for item in response['results']:
        character = {
            'name': item['name'],
            'no_of_episodes': len(item['episode'])
        }

        character_list.append(character)

    return character_list


data = main_request(baseurl, endpoint)
print(parse_json(data))


