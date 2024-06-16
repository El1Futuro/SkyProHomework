import os
from typing import Any

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_masks_for_card_number(card_number: str) -> str:
    """Функция, которая возвращает номер банковской карты в формате маски"""

    logger.info(f"Задаём формат маски для номера банковской карты {card_number}")

    number_with_spaces = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    return number_with_spaces


def get_masks_for_account_number(account_number: str) -> Any:
    """Функция, которая возвращает номер счёта в формате маски"""

    logger.info(f"Проверяем правильность написания {account_number}")
    if len(str(account_number)) != 20:
        logger.error("Ошибка. Проверьте номер счета, он должен содержать 20 цифр")
        raise ValueError("Проверьте номер счета, он должен содержать 20 цифр")

    else:
        logger.info(f"Задаём формат маски для номера банковского счета {account_number}")
        account_with_masks = account_number.replace(account_number[:-4], "*" * 2)

    return account_with_masks
