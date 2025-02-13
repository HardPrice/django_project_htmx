from django import template
from books.utils.get_exchange_currency import get_exchange_rate

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Умножает значение на аргумент.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None



@register.filter
def convert_currency(amount, currency_pair):
    """
    Конвертирует сумму из одной валюты в другую.
    :param amount: Сумма для конвертации
    :param currency_pair: Пара валют в формате 'USD-EUR'
    :return: Конвертированная сумма
    """
    base_currency, target_currency = currency_pair.split('-')
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        return round(float(amount) * rate, 2)
    return None