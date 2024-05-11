from typing import Any


def get_new_list(list_dict: list[dict[Any, str]], value='EXECUTED') -> list:
    """Функция, возвращающая только список словарей с заданным значением ключа"""

    new_list = []

    for my_dict in list_dict:
        if my_dict['state'] == value:
            new_list.append(my_dict)

    return new_list

print(get_new_list([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                   'EXECUTED'))
