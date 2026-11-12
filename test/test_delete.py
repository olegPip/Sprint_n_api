from api.listings_api import ListingsAPI


class TestDeleteListing:
    """Тесты удаления объявлений."""

    def test_successful_listing_deletion(self, user_token, created_listing_id):
        """Создатель успешно удаляет свое объявление."""
        response = ListingsAPI.delete_listing(user_token, created_listing_id)

        assert response.status_code == 200, (
            f"Не удалось удалить объявление: {response.status_code}; "
            f"ответ сервера: {response.text}"
        )

        response_data = response.json()
        assert response_data == {"message": "Объявление удалено успешно"}, (
            f"Неожиданный ответ при удалении: {response_data}"
        )


