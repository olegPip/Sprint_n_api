import pytest
from api.auth_api import AuthAPI
from utils.helpers import generate_unique_email
from data.test_data import DEFAULT_PASSWORD, DEFAULT_USERNAME


class TestRegistration:
    def test_successful_registration(self):
        """Успешная регистрация нового пользователя."""
        email = generate_unique_email()
        response = AuthAPI.register_user(email, DEFAULT_PASSWORD, DEFAULT_USERNAME)

        assert response.status_code == 201, (
            f"Ошибка регистрации: {response.status_code}; ответ сервера: {response.text}"
        )

        response_data = response.json()

        # Проверяем объект пользователя в ответе
        assert "user" in response_data, f"В ответе отсутствует блок 'user': {response_data}"
        assert response_data["user"].get("email") == email
        assert response_data["user"].get("name") == "User"
        assert isinstance(response_data["user"].get("id"), int)

        # Проверяем наличие токена
        if "token" in response_data:
            access_token = response_data["token"].get("access_token")
            assert isinstance(access_token, str) and len(access_token) > 0

    def test_registration_with_existing_email_fails(self, registered_user):
        """Ошибка при попытке регистрации с уже существующим email."""
        response = AuthAPI.register_user(
            registered_user["email"], DEFAULT_PASSWORD, DEFAULT_USERNAME
        )

        assert response.status_code in (400, 409), (
            f"Ожидался статус 400 или 409, получен {response.status_code}; ответ: {response.text}"
        )

        response_data = response.json()
        assert "message" in response_data or "detail" in response_data, (
            f"В ответе об ошибке отсутствует описание: {response_data}"
        )
        error_text = response_data.get("message") or response_data.get("detail")
        assert isinstance(error_text, str) and len(error_text) > 0
