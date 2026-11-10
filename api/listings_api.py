import requests
from data.test_data import BASE_URL


class ListingsAPI:
    @staticmethod
    def create_listing(token, data, verify_ssl=False):
        token_str = token.get("access_token") if isinstance(token, dict) else token

        headers = {
            "Authorization": f"Bearer {token_str}"
        }

        # Минимальный валидный байт-код картинки
        valid_gif_bytes = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'

        # Попробуем отправить файл как элемент массива "images",
        # бэкенд qa-desk часто принимает массив картинок и раскладывает их в img1, img2, img3 автоматически
        files = [
            ("images", ("pixel.gif", valid_gif_bytes, "image/gif"))
        ]

        # Преобразуем текстовые поля в строки
        form_data = {key: str(value) for key, value in data.items()}

        response = requests.post(
            f"{BASE_URL}/create-listing",
            data=form_data,
            files=files,
            headers=headers,
            verify=verify_ssl
        )
        return response

    @staticmethod
    def edit_listing(token, listing_id, update_data, verify_ssl=False):
        token_str = token.get("access_token") if isinstance(token, dict) else token
        headers = {
            "Authorization": f"Bearer {token_str}"
        }
        form_data = {key: str(value) for key, value in update_data.items()}

        return requests.patch(
            f"{BASE_URL}/update-offer/{listing_id}",
            data=form_data,
            headers=headers,
            verify=verify_ssl
        )

    @staticmethod
    def delete_listing(token, listing_id, verify_ssl=False):
        token_str = token.get("access_token") if isinstance(token, dict) else token
        headers = {"Authorization": f"Bearer {token_str}"}
        response = requests.delete(f"{BASE_URL}/listings/{listing_id}", headers=headers, verify=verify_ssl)
        return response

    @staticmethod
    def get_listings(verify_ssl=False):
        return requests.get(f"{BASE_URL}/listings", verify=verify_ssl)