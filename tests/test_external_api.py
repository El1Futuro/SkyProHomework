import os
import unittest
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.external_api import get_amount_rub

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


class TestGetAmountRub(unittest.TestCase):

    @patch("requests.get")
    def test_convert_usd_to_rub(self, mock_get: MagicMock) -> None:
        mock_get.return_value.json.return_value = {"result": 90.0}
        mock_get.return_value.status_code = 200
        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 90.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
        )

    @patch("requests.get")
    def test_convert_eur_to_rub(self, mock_get: MagicMock) -> None:
        mock_get.return_value.json.return_value = {"result": 105.0}
        mock_get.return_value.status_code = 200
        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "EUR"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 105.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1", headers={"apikey": API_KEY}
        )

    def test_convert_rub_to_rub(self) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 100)
