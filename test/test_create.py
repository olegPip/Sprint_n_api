import pytest
from api.listings_api import ListingsAPI
from data.test_data import DEFAULT_LISTING_DATA


class TestCreateListing:
    def test_successful_listing_creation(self, user_token):
        """Успешное создание объявления с валидными данными и проверкой ID."""
        response = ListingsAPI.create_listing(user_token, DEFAULT_LISTING_DATA)

        assert response.status_code == 201, f"Неверный статус-код! Ответ сервера: {response.text}"
        assert "id" in response.json()
