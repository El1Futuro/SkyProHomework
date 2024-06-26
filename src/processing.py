from typing import Any


def filter_transactions_by_state(list_transactions: list[dict[Any, Any]], value: str) -> list[dict[Any, Any]]:
    """Функция возвращает только список словарей с заданным значением ключа"""
    new_list = []

    for dicts in list_transactions:
        if "state" in dicts and dicts["state"] == value:
            new_list.append(dicts)

    return new_list


def get_sorted_list(list_dict: list[dict[Any, Any]], revers: bool) -> list[dict[Any, Any]]:
    """Функция возвращает список словарей, отсортированных по дате операции"""

    sorted_list = sorted(list_dict, key=lambda my_dict: my_dict["date"], reverse=revers)
    return sorted_list
