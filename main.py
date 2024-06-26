import datetime
import os
from typing import Any

import pandas as pd

from src.extra_functions import get_currency_sort, get_date_sort, get_status
from src.search_line import filter_operations
from src.utils import (
    get_list_transactions,
    get_transactions_from_csv,
    get_transactions_from_excel,
    transaction_csv_utils,
    transaction_xlsx_utils,
)

from src.external_api import get_amount_rub
from src.masks import get_masks_for_account_number, get_masks_for_card_number
from src.widget import get_date_string, get_mask_card_account

print(get_masks_for_card_number("7000792289606361"))
print(get_masks_for_account_number("73654108430135874305"))
print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("Visa Platinum 8990922113665229"))
print(get_date_string("2018-07-11T02:26:18.671407"))
print()

state_1 = "EXECUTED"
state_2 = "CANCELED"
state_3 = "PENDING"
state_request = "Введите статус, по которому необходимо выполнить фильтрацию."


def main() -> Any:
    greetings = "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(greetings)

    while True:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_choice = int(input())

        if user_choice == 1:
            json_file_path = os.path.join("data", "operations.json")
            list_transactions = get_list_transactions(json_file_path)
            print("Для обработки выбран JSON-файл.")

            print(state_request)
            print(f"Доступные для фильтровки статусы: {state_1}, {state_2}, {state_3}")
            user_choice_1 = input().upper()
            filtered_transactions = get_status(user_choice_1, list_transactions)
            break
        elif user_choice == 2:
            csv_file_path = os.path.join("data", "transactions.csv")
            list_transactions = transaction_csv_utils(get_transactions_from_csv(csv_file_path))
            print("Для обработки выбран CSV-файл.")

            print(state_request)
            print(f"Доступные для фильтровки статусы: {state_1}, {state_2}, {state_3}")
            user_choice_1 = input().upper()
            filtered_transactions = get_status(user_choice_1, list_transactions)
            break
        elif user_choice == 3:
            excel_file_path = os.path.join("data", "transactions_excel.xlsx")
            list_transactions = transaction_xlsx_utils(get_transactions_from_excel(excel_file_path))
            print("Для обработки выбран XLSX-файл.")

            print(state_request)
            print(f"Доступные для фильтровки статусы: {state_1}, {state_2}, {state_3}")
            user_choice_1 = input().upper()
            filtered_transactions = get_status(user_choice_1, list_transactions)
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    date_sort_question = "Отсортировать операции по дате? Да/Нет"
    print(date_sort_question)
    date_sort_ans = input().lower()

    direction_sort_question = "Отсортировать по возрастанию или по убыванию?"
    print(direction_sort_question)
    direction_sort_ans = input().lower()
    filtered_by_date_transactions = get_date_sort(date_sort_ans, filtered_transactions, direction_sort_ans)

    filtered_by_currency_transactions = get_currency_sort(filtered_by_date_transactions)

    word_sort_question = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
    print(word_sort_question)
    word_sort_ans = input().lower()

    def get_word_sort(word_sort_ans: str, filtered_by_currency_transactions: list) -> list:
        """Функция фильтрует полученный список по введенному пользователем слову для поиска"""
        while True:
            if word_sort_ans == "да":
                search_string = input("Введите слово для поиска: ")
                sorted_word_transactions = filter_operations(filtered_by_currency_transactions, search_string)
                return sorted_word_transactions
            elif word_sort_ans == "нет":
                return filtered_by_currency_transactions
            else:
                print("Некорректный выбор. Попробуйте еще раз.")
                continue

    result_sort = get_word_sort(word_sort_ans, filtered_by_currency_transactions)
    if not result_sort:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:

        print(f"Всего банковских операций в выборке: {len(result_sort)}")
        print("Распечатываю итоговый список транзакций...")
        print()
        for transaction in result_sort:
            date = datetime.datetime.fromisoformat(transaction["date"]).strftime("%d.%m.%Y")
            if "from" in transaction and pd.notnull(transaction["from"] or transaction["from"] is not None):
                from_ = get_mask_card_account(transaction["from"])
            else:
                from_ = ""
            to_ = get_mask_card_account(transaction["to"])
            description = transaction["description"]
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
            if currency == "Ruble":
                currency = "руб."
            print(f"{date} {description}\n{from_ or ""} -> {to_ or ""}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
