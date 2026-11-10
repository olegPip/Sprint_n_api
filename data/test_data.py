BASE_URL = "https://qa-desk.education-services.ru/api"


# Дефолтный пароль и имя для создаваемых пользователей
DEFAULT_PASSWORD = "TestPassword123!"
DEFAULT_USERNAME = "AutotestUser"

# Данные для дефолтного объявления
DEFAULT_LISTING_DATA = {
    "price": 300,
    "name": "Игрушки для кота",
    "category": "Хобби",
    "condition": "Новый",
    "city": "Казань",
    "description": "Коту не понравились, новые."
}

# Передаем полный набор полей, чтобы пройти валидацию схемы на бэкенде
UPDATED_LISTING_DATA = {
    "price": 250,
    "name": "Игрушки для кота (Обновлено)",
    "category": "Хобби",
    "condition": "Новый",
    "city": "Казань",
    "description": "Коту не понравились, новые."
}