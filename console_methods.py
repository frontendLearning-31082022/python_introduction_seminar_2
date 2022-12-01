import re
import sys


def input_strings_while_q(msg):
    print_console(msg + " <<<<To_STOP_-_enter_'q'>>>>")
    result = []
    inputed = ""
    while not inputed.__eq__("q"):
        inputed = input()
        if inputed.__eq__("q"): break
        result.append(inputed)

    return result


def input_one_string(msg):
    print_console(msg)
    inputed = input()
    return inputed


def input_dig_in_range(msg, from_dig, to_dig):
    if msg != None:
        print_console(msg)
    inputed = input_digit(True)
    while inputed <= from_dig >= to_dig:
        inputed = input_digit(True)
        print_console(f"in range {from_dig} to {to_dig} pls")
    return inputed


def input_digit(positive_only):
    while True:
        inputed = input()
        result = re.findall(r'\D', inputed)
        result = list(filter(lambda x: not (str(x).__eq__("-")), result))
        result = list(filter(lambda x: not (str(x).__eq__(",")), result))
        result = list(filter(lambda x: not (str(x).__eq__(".")), result))
        corrected_input = len(result) == 0
        if (positive_only and corrected_input):
            corrected_input = int(inputed) > -1
        if corrected_input:
            break
        print_console("Input integer again")

    inputed = int(inputed)
    return inputed


def print_console(textt='', *new_line):
    if new_line != None:
        sys.stdout.write(textt)
        return

    print(textt)
