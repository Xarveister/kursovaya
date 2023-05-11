# импорт библиотек и функций
import json
from datetime import datetime


# функция чтения файла json
def load_data():
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# функция сортирует по значению 'EXECUTED' ("выполнено")
def get_filtred_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


# функция сортирует по дате и выводит последние 5 операций
def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


# функция форматирует и выдает заданный результат
def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        recipient = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        else:
            from_info, from_bill = "", ""
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient}
{operation_amount}""")
    return formatted_data
