import pytest
from api.listings_api import ListingsAPI
from data.test_data import UPDATED_LISTING_DATA


class TestEditListing:
    """Тесты функциональности редактирования объявлений."""

    def test_successful_field_editing(self, user_token, created_listing_id):
        """Успешное редактирование полей объявления его создателем."""
        response = ListingsAPI.edit_listing(user_token, created_listing_id, UPDATED_LISTING_DATA)
        assert response.status_code == 200

        response_data = response.json()
        assert response_data["id"] == created_listing_id
        for key, expected_value in UPDATED_LISTING_DATA.items():
            assert response_data.get(key) == expected_value, (
                f"Поле '{key}' не обновилось: ожидалось {expected_value}, получено {response_data.get(key)}"
            )

    def test_edit_listing_by_another_user_fails(self, secondary_user_token, created_listing_id):
        """Ошибка авторизации при попытке изменить чужое объявление другим пользователем."""
        response = ListingsAPI.edit_listing(secondary_user_token, created_listing_id, UPDATED_LISTING_DATA)
        assert response.status_code == 401

        response_data = response.json()
        assert response_data["message"] == "Оффер не найден или у вас нет прав на его редактирование"
        assert response_data["error"] == "Unauthorized"
        assert response_data["statusCode"] == 401



