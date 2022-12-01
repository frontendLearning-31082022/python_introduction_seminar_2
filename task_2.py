# 2) Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
import console_methods

if __name__ == '__main__':
    inputed = console_methods.input_strings_while_q("Input elements for list")
    for x in range(0, len(inputed) - 1, 2):
        temp = inputed[x]
        inputed[x] = inputed[x + 1]
        inputed[x + 1] = temp

    console_methods.print_console("result")
    for vall in inputed:
        console_methods.print_console(vall)
