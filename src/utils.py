import csv
import json
import os
from typing import Any

import pandas
import pandas as pd

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


def get_transactions_from_csv(csv_file_path: str) -> Any:
    """Функция принимает путь до CSV-файла и возвращает данные финансовых транзакций"""

    logger.info(f"Открытие csv файла {csv_file_path}")
    try:
        data_list = []
        with open(csv_file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            logger.info(f"Проверяем, что файл {csv_file_path} не пустой")
            for row in reader:
                data_list.append(row)

            return data_list

    except Exception as e:
        logger.error(f"Ошибка, {e}.")

        return []


def get_transactions_from_excel(excel_file_path: str) -> Any:
    """Функция принимает путь до EXCEL-файла и возвращает данные финансовых транзакций"""
    try:
        excel_transactions = pd.read_excel(excel_file_path)
        logger.info(f"Проверяем, что файл {excel_file_path} не пустой")
        if isinstance(excel_transactions, pandas.DataFrame):
            excel_list = excel_transactions.to_dict("records")
            return excel_list
        else:
            logger.info(f"Пишет информационное сообщение, если файл {excel_file_path} пустой")
            print("File is empty")
    except Exception as e:
        logger.error("Ошибка", e)
        return []
