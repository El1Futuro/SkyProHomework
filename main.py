from src.decorators import log
from src.widget import get_mask_card_account, get_date_string


print(get_mask_card_account("Счет 64686473678894779589"))
print(get_mask_card_account("Visa Platinum 8990922113665229"))
print(get_date_string("2018-07-11T02:26:18.671407"))


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


@log()
def my_function_error(x, y):
    return x / y


my_function_error(2, 0)
