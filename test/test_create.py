import pytest
from api.listings_api import ListingsAPI
from data.test_data import DEFAULT_LISTING_DATA


class TestCreateListing:
    def test_successful_listing_creation(self, user_token):
        """Успешное создание объявления с валидными данными и проверкой тела ответа."""
        response = ListingsAPI.create_listing(user_token, DEFAULT_LISTING_DATA)

        assert response.status_code == 201, f"Неверный статус-код! Ответ сервера: {response.text}"

        response_data = response.json()

        # Проверяем наличие и корректность присвоенного ID
        assert "id" in response_data, f"В ответе отсутствует ключ 'id': {response_data}"
        assert isinstance(response_data["id"], int) and response_data["id"] > 0

        # Сверяем все отправленные поля с данными в ответе сервера
        for key, expected_value in DEFAULT_LISTING_DATA.items():
            assert response_data.get(key) == expected_value, (
                f"Поле '{key}' не совпадает: ожидалось {expected_value}, получено {response_data.get(key)}"
            )

