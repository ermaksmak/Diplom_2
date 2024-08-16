import requests
from data import Urls, ErrorMessage
from user_data import generate_user
import allure
class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Создаем пользователя, авторизовавшись с корректными e-mail и password,\
                        и проверяем, что код ответа: 200, и success = True')
    def test_login_user(self):
        payload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        del payload['name']
        response = requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=payload)
        assert response.status_code == 200 and response.json()['success'] == True
    @allure.title('Проверка авторизации пользователя с неправильным паролем')
    @allure.description('Создаем пользователя, авторизовавшись с неправильным password,\
                        и проверяем, что код ответа: 401, а текст ответа "email or password are incorrect"')
    def test_login_user_wrong_password(self):
        payload = generate_user()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        del payload['name']
        payload['password'] = 'wrong_password'
        response = requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=payload)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessage.text_login_401