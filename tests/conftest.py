import pytest

@pytest.fixture
def test_data():
    return [{
    "id": 10806000,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90817634362095555"
  },
  {
    "id": 100392079,
    "state": "EXECUTED",
    "date": "2018-03-03T03:13:18.622393",
    "operationAmount": {
      "amount": "44493.45",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Visa Classic 6319351940209800",
    "to": "Счет 14073196441261107791"
  }]
