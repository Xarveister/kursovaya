import pytest
from src.utils import load_data, get_filtred_data, get_last_values, get_formatted_data


def test_load_data():
    data = load_data()
    assert isinstance(data, list)


def test_get_filtred_data(test_data):
    assert get_filtred_data(test_data) == [{
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


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-06-21T12:34:06.351022', '2018-03-03T03:13:18.622393']


def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['21.06.2019 Открытие вклада\n  -> Счет **5555\n25762.92 руб.',
                    '03.03.2018 Перевод с карты на счет\n' 'Visa Classic 6319 35** **** 9800 -> Счет **7791\n'
                    '44493.45 USD']


