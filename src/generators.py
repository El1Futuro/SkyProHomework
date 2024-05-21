from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """Функция, которая принимает список словарей с банковскими операциями и
    возвращает итератор, выдающий по очереди операции в заданной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, Any, None]:
    """Функция создает генератор, принимающий список словарей и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Функция создает генератор номеров банковских карт, который генерирует номера карт в определенном формате"""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        card_number = f"{number[0:4]} {number[4:8]} {number[4:8]} {number[12:16]}"
        yield card_number
