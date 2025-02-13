import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_exchange_rate(base_currency, target_currency):
    """
    Получает курс обмена между двумя валютами.
    :param base_currency: Базовая валюта (например, 'USD')
    :param target_currency: Целевая валюта (например, 'RUB')
    :return: Курс обмена (float)
    """
    api_key = os.getenv('API_KEY_EXCHANGE_RATE')  # Замените на ваш ключ API
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rate']
        else:
            raise ValueError("Ошибка при получении курса валюты")
    except Exception as e:
        print(f"Ошибка: {e}")
        return None