import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
full_list = []


def main_request(baseurl, endpoint, page_no):
    page_no = f'?page={page_no}'
    r = requests.get(baseurl + endpoint + page_no)
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


data = main_request(baseurl, endpoint, 1)
for page in range(1, get_pages(data) + 1):
    #print(page)
    full_list.extend(parse_json(main_request(baseurl, endpoint, page)))

df = pd.DataFrame(full_list)

print(df.head(), df.tail())

