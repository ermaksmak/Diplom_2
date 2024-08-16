import pytest
import requests
from data import Urls, ErrorMessage
from user_data import generate_user
class TestCreateUser:
    def test_create_user(self):
        playload = generate_user()
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        token = response.json()['accessToken']
        requests.delete(f'{Urls.main_url}{Urls.api_delete_user}', headers={'Authorization': token})
        assert response.status_code == 200 and 'accessToken' in response.text (f'Ожидалось 200, получили {response.status_code}, \
                                                                                 ожидалось "accessToken", получили {response.text}')
    def test_create_user_double(self):
        playload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        assert response.status_code == 400 and response.text == ErrorMessage.text_create_403_double

    def test_create_user_without_name(self):
        payload= generate_user()
        del payload['name']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert response.status_code == 400 and response.text == ErrorMessage.text_create_403_wrong

    def test_create_user_without_email(self):
        payload= generate_user()
        del payload['email']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert response.status_code == 400 and response.text == ErrorMessage.text_create_403_wrong
    def test_create_user_without_password(self):
        payload= generate_user()
        del payload['password']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert response.status_code == 400 and response.text == ErrorMessage.text_create_403_wrong