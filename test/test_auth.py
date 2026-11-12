import pytest
from api.auth_api import AuthAPI


class TestAuth:
    def test_successful_authorization(self, registered_user):
        """Успешная авторизация зарегистрированного пользователя."""
        response = AuthAPI.login_user(registered_user["email"], registered_user["password"])

        assert response.status_code == 201, (
            f"Ошибка авторизации: {response.status_code}; ответ сервера: {response.text}"
        )

        response_data = response.json()

        # Проверяем вложенный токен
        assert "token" in response_data, f"В ответе отсутствует ключ 'token': {response_data}"
        assert "access_token" in response_data["token"], (
            f"В объекте 'token' отсутствует 'access_token': {response_data['token']}"
        )
        access_token = response_data["token"]["access_token"]
        assert isinstance(access_token, str) and len(access_token) > 0, "Токен должен быть непустой строкой"

        # Проверяем данные пользователя в ответе
        assert "user" in response_data, f"В ответе отсутствует ключ 'user': {response_data}"
        assert response_data["user"]["email"] == registered_user["email"]
        assert isinstance(response_data["user"]["id"], int)
