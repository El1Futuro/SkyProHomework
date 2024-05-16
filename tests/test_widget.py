import pytest


from src.widget import get_mask_card_account


@pytest.mark.parametrize("user_data, expected_result",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                             ("Счет 35383033474447895560", "Счет **5560"),
                             ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                             ])
def test_get_mask_card_account(user_data, expected_result):
    assert get_mask_card_account(user_data) == expected_result
