import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
full_list = []


def main_request(baseurl, endpoint, page_no):
    page_no = f'?page={page_no}'
    try:
        r = requests.get(baseurl + endpoint + page_no)
    except BaseException:
        print("Failed to retrieve data")

    return r.json()


def get_pages(response):
    return response['info']['pages']


def parse_json(response):
    character_list = []
    for item in response['results']:
        character = {
            'id': item['id'],
            'name': item['name'],
            'no_of_episodes': len(item['episode'])
        }

        character_list.append(character)

    return character_list

try:
    print('Attempting to fetch data')
    data = main_request(baseurl, endpoint, 1)
    for page in range(1, get_pages(data) + 1):
        full_list.extend(parse_json(main_request(baseurl, endpoint, page)))
    print('Successfully fetched the data')
    try:
        print("Attempting to create csv")
        df = pd.DataFrame(full_list)
        df.to_csv('characterlist.csv', index=False)
        print('Successfully created csv')
    except BaseException:
        print('Failed to create csv')
except BaseException:
    print('Unable to fetch data')



