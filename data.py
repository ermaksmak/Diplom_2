from faker import Faker
from random import randint


class Data:
    Faker.seed(randint(1000, 10000))
    faker = Faker()
    f_hash = faker.md5(raw_output=False)
    login = faker.name()
    email = faker.email()

class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    API_CREATE_USER = "/api/auth/register"
    API_LOGIN = "/api/auth/login"
    API_ORDER = "/api/v1/orders"
    API_DELETE_USER = "/api/auth/user"
    API_GET_USER = '/api/auth/user'
    API_GET_INGREDIENTS = "/api/ingredients"
    API_CREATE_ORDERS = "/api/orders"

class ErrorMessage:
    TEXT_LOGIN_401 = 'email or password are incorrect'
    TEXT_LOGIN_404 = "Учетная запись не найдена"
    TEXT_CREATE_403_DOUBLE = "User already exists"
    TEXT_CREATE_403_WRONG = "Email, password and name are required fields"
    TEXT_CREATE_400 = "Недостаточно данных для создания учетной записи"
    TEXT_UPDATE_401 = "You should be authorised"
    TEXT_ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
    TEXT_GET_ORDERS_NO_AUTH = "You should be authorised"

class Burgers:
    MET_FLU_CLASSIC = 'Метеоритный флюоресцентный традиционный-галактический бургер'
    SPACE_MARS = 'Space бессмертный био-марсианский бургер'
    SPICY = 'Spicy бессмертный краторный бургер'
