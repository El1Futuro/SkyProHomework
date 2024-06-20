import os

from src.utils import get_list_transactions, get_transactions_from_csv, get_transactions_from_excel
from src.external_api import get_amount_rub
from src.masks import get_masks_for_account_number, get_masks_for_card_number
from src.widget import get_date_string, get_mask_card_account


print(get_masks_for_card_number("7000792289606361"))
print(get_masks_for_account_number("73654108430135874305"))

print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("Visa Platinum 8990922113665229"))
print(get_date_string("2018-07-11T02:26:18.671407"))

print()

csv_file_path = os.path.join("data", "transactions.csv")
csv_transactions = get_transactions_from_csv(csv_file_path)
print(csv_transactions)

print()

excel_file_path = os.path.join("data", "transactions_excel.xlsx")
excel_transactions = get_transactions_from_excel(excel_file_path)
print(excel_transactions)

print()

json_file_path = os.path.join("data", "operations.json")
transactions = get_list_transactions(json_file_path)
print(transactions)

print()

for transaction in transactions:
    rub_amount = get_amount_rub(transaction)
    print(f"Транзакция в RUB: {rub_amount}")
