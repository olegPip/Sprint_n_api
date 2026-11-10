import pytest
from api.auth_api import AuthAPI
from utils.helpers import generate_unique_email
from data.test_data import DEFAULT_PASSWORD, DEFAULT_USERNAME

class TestRegistration:
    def test_successful_registration(self):
        email = generate_unique_email()
        response = AuthAPI.register_user(email, DEFAULT_PASSWORD, DEFAULT_USERNAME)
        assert response.status_code == 201

    def test_registration_with_existing_email_fails(self, registered_user):
        # Попытка зарегистрировать уже существующий в фикстуре email
        response = AuthAPI.register_user(registered_user["email"], DEFAULT_PASSWORD, DEFAULT_USERNAME)
        assert response.status_code == 400 or response.status_code == 409
