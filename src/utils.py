import json


def get_list_transactions(json_file_path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает данные финансовых транзакций"""
    # noinspection PyBroadException
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            list_transactions = json.load(file)
            if isinstance(list_transactions, list):
                return list_transactions
            else:
                return []

    except Exception:
        return []
