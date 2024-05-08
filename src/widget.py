from src.masks import get_masks_for_card_number, get_masks_for_account_number


def get_mask_card_account(user_data: str) -> str:
    """Функция получает на вход строку с данными счета/карты и возвращает их в формате маски"""

    if "Счет" in user_data:
        mask_account = get_masks_for_account_number(user_data.split()[-1])
        result = f"{user_data[0:5]} {mask_account}"
        return result

    else:
        mask_card = get_masks_for_card_number(user_data.split()[-1])
        result = f"{user_data[0:-16]} {mask_card}"
        return result

def get_date_string(user_date_time: str) -> str:
    user_date = user_date_time[0:10].split("-")
    correct_date = ".".join(user_date[::-1])
    return correct_date


print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("MasterCard 7158300734726758"))
print(get_date_string("2018-07-11T02:26:18.671407"))