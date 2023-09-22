import pytest
import yaml
import requests


with open('config.yaml', encoding='utf-8') as f:
    my_dict=yaml.safe_load(f)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def user_login():
     obj_data = requests.post(url=url, data={'username':'login', 'password': 'password'})
     token = obj_data.json()['token']
     return token

@pytest.fixture()
def postP():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'login',
        'password': 'password',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'we will see'})
    return obj_data.json()['description']