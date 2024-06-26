from src.processing import filter_transactions_by_state, get_sorted_list

state_1 = "EXECUTED"
state_2 = "CANCELED"
state_3 = "PENDING"
state_request = "Введите статус, по которому необходимо выполнить фильтрацию."


def filter_by_currency(transactions: list[dict], currency_code: str) -> list[dict]:
    """Функция, которая принимает список словарей с банковскими операциями и
    возвращает список словарей только в заданной валюте."""
    filtered_transactions = []
    for transaction in transactions:
        if transaction in transactions and transaction["operationAmount"]["currency"]["code"] == currency_code:
            filtered_transactions.append(transaction)
    return filtered_transactions


def get_status(user_choice_1: str, list_transactions: list) -> list:
    """Функция фильтрует полученный список по выбранному пользователем статусу"""
    if user_choice_1 in [state_1, state_2, state_3]:
        filtered_by_state_transactions = filter_transactions_by_state(list_transactions, user_choice_1)
        print(f"Операции отфильтрованы по статусу {user_choice_1}.")
        return filtered_by_state_transactions
    else:
        print(f"Статус операции {user_choice_1} недоступен.")
        print(state_request)
        print(f"Доступные для фильтровки статусы: {state_1}, {state_2}, {state_3}")
        user_choice_1 = input().upper()
        return get_status(user_choice_1, list_transactions)


def get_date_sort(date_sort_ans: str, filtered_by_state_transactions: list, direction_sort_ans: str) -> list:
    """Функция сортирует полученный список по выбранному пользователем критерию по убыванию или по возрастанию даты"""
    if date_sort_ans == "да":
        if direction_sort_ans == "по убыванию":
            sorted_transactions = get_sorted_list(filtered_by_state_transactions, revers=True)
            return sorted_transactions
        elif direction_sort_ans == "по возрастанию":
            sorted_transactions = get_sorted_list(filtered_by_state_transactions, revers=False)
            return sorted_transactions
        else:
            print(f"Статус операции {direction_sort_ans} недоступен.")
            return filtered_by_state_transactions
    else:
        return filtered_by_state_transactions


def get_currency_sort(filtered_by_date_transactions: list) -> list:
    """Функция фильтрует полученный список по заданной валюте"""
    while True:
        currency_sort_question = "Выводить только рублевые транзакции? Да/Нет"
        print(currency_sort_question)
        currency_sort_ans = input().lower()

        if currency_sort_ans == "да":
            sorted_currency_transactions = filter_by_currency(filtered_by_date_transactions, "RUB")
            if not sorted_currency_transactions:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
                continue
            return sorted_currency_transactions
        else:
            return filtered_by_date_transactions
