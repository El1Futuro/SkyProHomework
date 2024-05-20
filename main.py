from src.masks import get_masks_for_account_number, get_masks_for_card_number
from src.widget import get_date_string, get_mask_card_account
from src.processing import get_new_list, get_sorted_list

print(get_masks_for_card_number("7000792289606361"))
print(get_masks_for_account_number("73654108430135874305"))

print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("Visa Platinum 8990922113665229"))
print(get_date_string("2018-07-11T02:26:18.671407"))


print(get_new_list([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                   'EXECUTED'))

print(get_sorted_list([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], revers=True
                      ))
