import json
import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


def get_list_transactions(json_file_path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает данные финансовых транзакций"""
    # noinspection PyBroadException
    try:
        logger.info(f"Открытие json файла {json_file_path}")
        with open(json_file_path, "r", encoding="utf-8") as file:
            list_transactions = json.load(file)
            logger.info(f"Проверяем, что файл {json_file_path} не пустой")
            if isinstance(list_transactions, list):
                return list_transactions
            else:
                logger.info(f"Возвращаем пустой словарь, если файл {json_file_path} пустой")
                return []

    except Exception:
        logger.error("Ошибка")
        return []
