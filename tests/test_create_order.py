import requests
from data import Data, Urls, ErrorMessage, Burgers

class TestCreateOrder:
    def test_create_order_with_auth(self, create_user_and_get_token, get_ingredient_hash):
        requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=create_user_and_get_token)
        ingredients = {'ingredients': [get_ingredient_hash['data'][0]['_id'], get_ingredient_hash['data'][2]['_id'], get_ingredient_hash['data'][7]['_id']]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        order = response.json()
        assert order['name'] == Burgers.met_flu_classic and order['success'] == True
    def test_create_order_wihtout_auth(self, get_ingredient_hash):
        ingredients = {'ingredients': [get_ingredient_hash['data'][1]['_id'], get_ingredient_hash['data'][3]['_id'], get_ingredient_hash['data'][6]['_id']]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        order = response.json()
        assert order['name'] == Burgers.space_mars and order['success'] == True
