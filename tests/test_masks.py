import pytest

from src.masks import get_masks_for_account_number


def test_get_masks_for_account_number() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_masks_for_account_number("7365410843013587430")

    assert str(exc_info.value) == "Проверьте номер счета, он должен содержать 20 цифр"
