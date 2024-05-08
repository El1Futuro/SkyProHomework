def get_masks_for_card_number(card_number: str) -> str:
    """Функция, которая возвращает номер банковской карты в формате маски"""

    number_with_spaces = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    return number_with_spaces


def get_masks_for_account_number(account_number: str) -> str:
    """Функция, которая возвращает номер счёта в формате маски"""

    account_with_masks = account_number.replace(account_number[:-4], "*" * 2)

    return account_with_masks
