import pytest


from src.widget import get_mask_card_account, get_date_string


@pytest.mark.parametrize("user_data, expected_result",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                             ("Счет 35383033474447895560", "Счет **5560"),
                             ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")])
def test_get_mask_card_account(user_data, expected_result):
    assert get_mask_card_account(user_data) == expected_result


@pytest.mark.parametrize("user_date_time, correct_date",
                         [("2018-07-11T02:26:18.671407", "11.07.2018"),
                             ("2024-02-28T01:13:15.158707", "28.02.2024")])
def test_get_date_string(user_date_time, correct_date):
    assert get_date_string(user_date_time) == correct_date
