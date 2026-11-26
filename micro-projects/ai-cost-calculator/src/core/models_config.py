# core/models_config.py

# Тарифы указаны за 1 000 000 (1М) токенов в USD
PRICES = {
    "LLM1": {
        "price_in": 2.50,
        "price_out": 10.00
    },
    "LLM2": {
        "price_in": 3.00,
        "price_out": 15.00
    },
    "LLM3": {
        "price_in": 0.14,
        "price_out": 0.28
    },
    "custom-default": {
        "price_in": 3.00,
        "price_out": 15.00
    }
}

def get_rates(model_name="custom-default"):
    """
    Возвращает тарифы для указанной модели.
    Если модель не найдена, возвращает дефолтные тарифы.
    """
    return PRICES.get(model_name, PRICES["custom-default"])
