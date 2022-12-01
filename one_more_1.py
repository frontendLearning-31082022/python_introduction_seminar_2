# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
import re

import console_methods

if __name__ == '__main__':
    dig = console_methods.input_digit(False)
    result = re.findall(r'\d', str(dig))
    total = sum(map(int, result))
    console_methods.print_console("Sum digits " + str(total))
