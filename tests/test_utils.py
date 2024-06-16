import unittest
from unittest.mock import MagicMock, patch

from src.utils import get_list_transactions


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
