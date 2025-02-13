# context_processors.py
from books.utils.get_exchange_currency import get_exchange_rate

def exchange_rates(request):
    """
    Добавляет курсы валют в контекст шаблона.
    """
    rates = {
        'usd_to_rub': get_exchange_rate('USD', 'RUB'),
    }
    return {'exchange_rates': rates}