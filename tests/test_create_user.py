import pytest
import requests
import allure
from data import Urls, ErrorMessage
from user_data import generate_user
class TestCreateUser:

    @allure.title('Проверка успешной регистрации нового пользователя')
    @allure.description('Создаем пользователя, проверяем, что код ответа: 200,\
                            и в тексте ответа содержится accessToken')
    def test_create_user(self):
        playload = generate_user()
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        token = response.json()['accessToken']
        requests.delete(f'{Urls.main_url}{Urls.api_delete_user}', headers={'Authorization': token})
        assert response.status_code == 200 and 'accessToken' in response.text, (f'Ожидалось 200, получили {response.status_code}, \
                                                                                 ожидалось "accessToken", получили {response.text}')

    @allure.title('Проверка повторной регистрации пользователя')
    @allure.description('Создаем пользователя, проверяем, что код ответа: 403,\
                            и проверяем, что код ответа: 403, и текст ответа "User already exists"')
    def test_create_user_double(self):
        playload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=playload)
        assert 403 == response.status_code and  response.json()['message'] == ErrorMessage.text_create_403_double

    @allure.title('Проверка регистрации пользователя без имени')
    @allure.description('Создаем пользователя с пустым полем name, \
                        проверяем, что код ответа: 403, и текст ответа "Email, password and name are required fields"')
    def test_create_user_without_name(self):
        payload = generate_user()
        del payload['name']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert 403 == response.status_code and response.json()['message'] == ErrorMessage.text_create_403_wrong

    @allure.title('Проверка регистрации пользователя без почты')
    @allure.description('Создаем пользователя с пустым полем email, \
                           проверяем, что код ответа: 403, и текст ответа "Email, password and name are required fields"')
    def test_create_user_without_email(self):
        payload= generate_user()
        del payload['email']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert 403 == response.status_code and response.json()['message'] == ErrorMessage.text_create_403_wrong

    @allure.title('Проверка регистрации пользователя без пароля')
    @allure.description('Создаем пользователя с пустым полем password, \
                               проверяем, что код ответа: 403, и текст ответа "Email, password and name are required fields"')
    def test_create_user_without_password(self):
        payload= generate_user()
        del payload['password']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data={})
        assert 403 == response.status_code and response.json()['message'] == ErrorMessage.text_create_403_wrong