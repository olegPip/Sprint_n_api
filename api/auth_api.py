import requests
from data.test_data import BASE_URL

class AuthAPI:
    @staticmethod
    def register_user(email, password, username, verify_ssl=False):
        payload = {
            "email": email,
            "password": password,
            "username": username
        }
        # Формирует идеальный: https://education-services.ru
        return requests.post(f"{BASE_URL}/signup", json=payload, verify=verify_ssl)

    @staticmethod
    def login_user(email, password, verify_ssl=False):
        payload = {
            "email": email,
            "password": password
        }
        # Формирует идеальный: https://qa-desk.education-services.ru/api/signin
        return requests.post(f"{BASE_URL}/signin", json=payload, verify=verify_ssl)

