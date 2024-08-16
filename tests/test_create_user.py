import pytest
import requests
from data import Urls, ErrorMessage
from user_data import generate_user
class TestCreateUser:
    def test_create_user(self, create_user_and_get_token):
        playload = generate_user()
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        token = response.json()['accessToken']
        requests.delete(f'{Urls.main_url}{Urls.api_delete_user}', headers={'Authorization': token})
        assert response.status_code == 200 and 'accessToken' in response.text (f'Ожидалось 200, получили {response.status_code}, \
                                                                                 ожидалось "accessToken", получили {response.text}')