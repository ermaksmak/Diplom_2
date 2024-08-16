import requests

from data import Urls, ErrorMessage


class TestGetOrders:
    def test_get_order_without_auth_faild(self):
        response = requests.get(f'{Urls.main_url}{Urls.api_create_order}')
        assert response.status_code == 401 and response.json()['message'] == ErrorMessage.text_get_orders_no_auth

    def test_order_auth_success(self, create_user_and_get_token, get_ingredient_hash):
        token = create_user_and_get_token
        ingredients = {'ingredients': [get_ingredient_hash['data'][0]['_id'], get_ingredient_hash['data'][2]['_id'], get_ingredient_hash['data'][7]['_id']]}
        requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        response = requests.get(f'{Urls.main_url}{Urls.api_create_order}', headers={'Authorization':token})
        assert response.status_code == 200 and "orders" in response.text
