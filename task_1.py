# 1) Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.


if __name__ == '__main__':
    final_vars = ('password',)

    list = ["", ""]
    hash_map = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
    set_empty = set()
    set_var = set('bug generator ready')
    low_case_madness = True
    types_various = [10, "String_var", list, final_vars, low_case_madness,
                     set_var, hash_map]

    for elem in types_various:
        print("what's it - " + str(type(elem)) + "\n")
