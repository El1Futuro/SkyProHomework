import requests
import os
from typing import Any
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def get_amount_rub(transactions: dict) -> Any:
    """Функция принимает транзакцию и возвращает сумму этой транзакции, конвертируя при необходимости ее в рубли,
    используя обращение к внешнему API для получения текущего курса валют"""
    amount = transactions.get("operationAmount", {}).get("amount")
    currency = transactions.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        response = requests.get(API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY})
        if response.status_code == 200:
            data = response.json()
            return data["result"]
        else:
            return 0.0
    else:
        return 0.0
