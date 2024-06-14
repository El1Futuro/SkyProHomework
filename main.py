import os
from src.utils import get_list_transactions
from src.widget import get_mask_card_account, get_date_string
from src.external_api import get_amount_rub




print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("Visa Platinum 8990922113665229"))
print(get_date_string("2018-07-11T02:26:18.671407"))


print()

json_file_path = os.path.join("data", "operations.json")
transactions = get_list_transactions(json_file_path)
print(transactions)

print()

for transaction in transactions:
    rub_amount = get_amount_rub(transaction)
    print(f"Транзакция в RUB: {rub_amount}")
