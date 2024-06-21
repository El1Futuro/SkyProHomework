import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.utils import get_list_transactions, get_transactions_from_csv, get_transactions_from_excel


class TestGetListTransactions(unittest.TestCase):

    @patch("builtins.open")
    def test_get_list_transactions_valid_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
        list_transactions = get_list_transactions("test_file.json")
        self.assertEqual(list_transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_get_list_transactions_empty_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        list_transactions = get_list_transactions("test_file.json")
        self.assertEqual(list_transactions, [])

    def test_get_list_transactions_file_not_found(self) -> None:
        list_transactions = get_list_transactions("nonexistent_file.json")
        self.assertEqual(list_transactions, [])


class TestGetTransactionsFromCsv(unittest.TestCase):

    def test_get_transactions_from_csv_file_not_found(self) -> None:
        csv_transactions = get_transactions_from_csv("nonexistent_file.csv")
        self.assertEqual(csv_transactions, [])

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover 7269000803370165;"
        "American Express 1963030970727681;Перевод с карты на карту\n",
    )
    def test_get_transactions_from_csv_new(self, mock_file: MagicMock) -> None:
        result = get_transactions_from_csv("test.csv")
        self.assertEqual(
            result,
            [
                {
                    "id": "4699552",
                    "state": "EXECUTED",
                    "date": "2022-03-23T08:29:37Z",
                    "amount": "23423",
                    "currency_name": "Peso",
                    "currency_code": "PHP",
                    "description": "Перевод с карты на карту",
                    "from": "Discover 7269000803370165",
                    "to": "American Express 1963030970727681",
                }
            ],
        )

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_transactions_from_csv_new_1(self, mock_file: MagicMock) -> None:
        result = get_transactions_from_csv("test.csv")
        self.assertEqual(result, [])

    data = {
        "id": [4699552.0],
        "state": ["EXECUTED"],
        "date": ["2022-03-23T08:29:37Z"],
        "amount": [23423.0],
        "currency_name": ["Peso"],
        "currency_code": ["PHP"],
        "from": ["Discover 7269000803370165"],
        "to": ["American Express 1963030970727681"],
        "description": ["Перевод с карты на карту"],
    }

    df = pd.DataFrame(data)

    df.to_excel("test.xlsx", index=False)

    @patch("pandas.read_excel", return_value=df)
    def test_get_transactions_from_excel(self, mock_read: MagicMock) -> None:
        result = get_transactions_from_excel("test.xlsx")
        self.assertEqual(
            result,
            [
                {
                    "id": 4699552,
                    "state": "EXECUTED",
                    "date": "2022-03-23T08:29:37Z",
                    "amount": 23423.0,
                    "currency_name": "Peso",
                    "currency_code": "PHP",
                    "description": "Перевод с карты на карту",
                    "from": "Discover 7269000803370165",
                    "to": "American Express 1963030970727681",
                }
            ],
        )
