from faker import Faker
from random import randint


class Data:
    Faker.seed(randint(1000, 10000))
    faker = Faker()
    f_hash = faker.md5(raw_output=False)
    login = faker.name()
    email = faker.email()

class Urls:
    main_url = "https://stellarburgers.nomoreparties.site"
    api_create_user = "/api/auth/register"
    api_login_user = "/api/auth/login"
    api_order = "/api/v1/orders"
    api_delete_user = "/api/auth/user"
    api_get_user = '/api/auth/user'
    api_get_ingredients = "/api/ingredients"
    api_create_order = "/api/orders"
