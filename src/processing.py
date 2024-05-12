from typing import Any


def get_new_list(list_dict: list[dict[Any, str]], value='EXECUTED') -> list:
    """Функция, возвращающая только список словарей с заданным значением ключа"""

    new_list = []

    for my_dict in list_dict:
        if my_dict['state'] == value:
            new_list.append(my_dict)

    return new_list


def get_sorted_list(list_dict: list[dict[Any, str]], reverse=True) -> Any:
    """Функция возвращает список словарей, отсортированных по дате операции"""

    return sorted(list_dict, key=lambda my_dict: my_dict['date'], reverse=True)
