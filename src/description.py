from collections import Counter

from src.utils import get_list_transactions

json_file_path = r"C:\Users\User\PycharmProjects\SecondHomework1\data\operations.json"
list_transactions = get_list_transactions(json_file_path)


def get_categories(list_transactions: list) -> list:
    """Функция возвращает список всех категорий из поля 'description' в списке транзакций"""
    categories = set()
    for transaction in list_transactions:
        if "description" in transaction:
            categories.add(transaction["description"])
    list_categories = list(categories)
    return list_categories


def count_operations_by_category(list_transactions: list, list_categories: list) -> dict:
    """Функция выводит словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории⠀"""
    counter = Counter()
    for transaction in list_transactions:
        if "description" in transaction:
            if transaction["description"] in list_categories:
                counter[transaction["description"]] += 1
    return dict(counter)


if __name__ == "__main__":

    get_categories(list_transactions)
    print(count_operations_by_category(list_transactions, get_categories(list_transactions)))
