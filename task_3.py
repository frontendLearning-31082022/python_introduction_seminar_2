# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
import console_methods

if __name__ == '__main__':
    list_way = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring'
        , 'Summer', 'Summer', 'Summer'
        , 'Autumn', 'Autumn', 'Autumn', 'Winter']

    dig = console_methods.input_dig_in_range("Input digit", 1, 12)

    print(f"List-- {dig} it's {list_way[dig - 1]}")

    dict_way = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter',
    }
    print(f"Dict-- {dig} it's {dict_way[dig - 1]}")
