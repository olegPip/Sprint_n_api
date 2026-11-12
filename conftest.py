import pytest
from utils.helpers import generate_unique_email
from data.test_data import DEFAULT_PASSWORD, DEFAULT_USERNAME, DEFAULT_LISTING_DATA
from api.auth_api import AuthAPI
from api.listings_api import ListingsAPI

@pytest.fixture
def registered_user():
    """Регистрирует случайного пользователя и возвращает его учетные данные."""
    email = generate_unique_email()
    AuthAPI.register_user(email, DEFAULT_PASSWORD, DEFAULT_USERNAME)
    return {"email": email, "password": DEFAULT_PASSWORD, "username": DEFAULT_USERNAME}

@pytest.fixture
def user_token(registered_user):
    """Авторизует пользователя и возвращает его Bearer-токен."""
    response = AuthAPI.login_user(registered_user["email"], registered_user["password"])
    return response.json()["token"]

@pytest.fixture
def secondary_user_token():
    """Создает токен второго (чужого) пользователя для проверки прав доступа."""
    email = generate_unique_email()
    AuthAPI.register_user(email, DEFAULT_PASSWORD, "SecondaryUser")
    response = AuthAPI.login_user(email, DEFAULT_PASSWORD)
    return response.json()["token"]

@pytest.fixture
def created_listing_id(user_token):
    """Предусловие: Создает объявление под основным токеном и возвращает его ID."""
    response = ListingsAPI.create_listing(user_token, DEFAULT_LISTING_DATA)
    return response.json()["id"]
