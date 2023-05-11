# импорт функций
from utils import get_filtred_data, load_data, get_last_values, get_formatted_data


# основная функция, вызывающая последовательно все функции
def main():
    count_last_values = 5
    data = load_data()
    data = get_filtred_data(data)
    data = get_last_values(data, count_last_values)
    data = get_formatted_data(data)
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
