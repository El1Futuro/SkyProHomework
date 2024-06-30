import re

from src.utils import get_list_transactions

json_file_path = r"C:\Users\Admin\PycharmProjects\SecondHomework1\data\operations.json"
list_transactions = get_list_transactions(json_file_path)


def filter_operations(list_transactions: list, search_string: str) -> list:
    """Функция фильтрует полученный список по введенному пользователем слову для поиска"""
    filtered_list = []
    for dicts in list_transactions:
        description = dicts.get("description", "")
        if re.search(search_string, description, re.IGNORECASE):
            filtered_list.append(dicts)
    return filtered_list
