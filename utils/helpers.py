import uuid

def generate_unique_email() -> str:
    """Генерирует гарантированно уникальный email для каждого теста."""
    return f"user_{uuid.uuid4().hex[:8]}@qa-desk.ru"
