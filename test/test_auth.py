import pytest
from api.auth_api import AuthAPI

class TestAuth:
    def test_successful_authorization(self, registered_user):
        response = AuthAPI.login_user(registered_user["email"], registered_user["password"])
        assert response.status_code == 201
        assert "token" in response.text or "access_token" in response.text
