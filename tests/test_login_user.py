import requests
from data import Urls, ErrorMessage
from user_data import generate_user

class TestLoginUser:

    def test_login_user(self):
        payload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        del payload['name']
        response = requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=payload)
        assert response.status_code == 200 and response.json()['success'] == True
    def test_login_user_wrong_password(self):
        payload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        del payload['name']
        payload['password'] = 'wrong_password'
        response = requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=payload)
        assert response.status_code == 400 and response.text == ErrorMessage.text_login_401