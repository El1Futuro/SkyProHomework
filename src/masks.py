from typing import Any


def get_masks_for_card_number(card_number: str) -> str:
    """Функция, которая возвращает номер банковской карты в формате маски"""

    number_with_spaces = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    return number_with_spaces


def get_masks_for_account_number(account_number: str) -> Any:
    """Функция, которая возвращает номер счёта в формате маски"""

    def get_length_account_number(account_number):
        if len(str(account_number)) != 20:
            raise ValueError("Проверьте номер счета, он должен содержать 20 цифр")

    get_length_account_number(account_number)

    account_with_masks = account_number.replace(account_number[:-4], "*" * 2)

    return account_with_masks
