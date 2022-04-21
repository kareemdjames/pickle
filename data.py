import shutil
import requests
import pandas as pd
import os
from google.cloud import storage

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
full_list = []
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'pickle-347602-fb0b2dc2eb0d.json'
client = storage.Client()




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
            'char_name': item['name'],
            'no_of_episodes': len(item['episode']),
            'image': item['image']
        }

        character_list.append(character)

    return character_list


# def start():
#     try:
#         print('Attempting to fetch data')
#         data = main_request(baseurl, endpoint, 1)
#         for page in range(1, get_pages(data) + 1):
#             full_list.extend(parse_json(main_request(baseurl, endpoint, page)))
#         print('Successfully fetched the data')
#         try:
#             print("Attempting to create csv")
#             df = pd.DataFrame(full_list)
#             df.to_csv('characterlist.csv', index=False)
#             print('Successfully created csv')
#         except BaseException:
#             print('Failed to create csv')
#     except BaseException:
#         print('Unable to fetch data')
#
#     return full_list


def get_image_urls():
    df = pd.read_csv('characterlist.csv', nrows=10)
    print(df.to_string())
    row_list = []
    for i, rows in df.iterrows():
        url_and_name_list = [rows.char_name, rows.image]
        row_list.append(url_and_name_list)
    print(row_list)
    return row_list


def download_images(list_of_images):
    for row in list_of_images:
        name = row[0]
        image_url = row[1]
        file_name = name + '.jpeg'
        res = requests.get(image_url, stream=True)

        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
        else:
            print('Image Couldn\'t be retrieved')


#download_images(get_image_urls())
# get_image_urls()