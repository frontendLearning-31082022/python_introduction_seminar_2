# 5) Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат:         7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат:         8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат:         7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].
import console_methods


class Node_one_way:
    def __init__(self):
        self.value_cell = None
        self.next = None


class RatingStructure:
    __head = Node_one_way()

    @classmethod
    def get_value(self, object_node: Node_one_way):
        return object_node.value_cell

    def __init__(self, my_list):

        for node_index in range(0, len(my_list)):
            self.insert_node(my_list[node_index])

    def insert_node(self, value_cell):
        new_node = Node_one_way()  # create a new node
        new_node.value_cell = value_cell

        if self.__head.value_cell == None:
            self.__head = new_node
            return

        if new_node.value_cell > self.__head.value_cell:
            new_node.next = self.__head
            self.__head = new_node
            return

        find_last = self.__head
        while find_last.next != None:
            next_digit = RatingStructure.get_value(find_last.next)
            if next_digit < new_node.value_cell:
                new_node.next = find_last.next
                find_last.next = new_node
                return
            find_last = find_last.next

        find_last.next = new_node

    def print_chain(self):
        find_last = self.__head
        console_methods.print_console("[" + str(find_last.value_cell))
        while find_last.next != None:
            console_methods.print_console(",", True)
            find_last = find_last.next
            console_methods.print_console(str(find_last.value_cell))
        console_methods.print_console("]", True)


def test_drive(rating):
    rating.insert_node(8)
    rating.insert_node(3)
    rating.insert_node(1)
    rating.insert_node(9)
    rating.insert_node(5)
    rating.insert_node(4)


if __name__ == '__main__':
    my_list = [7, 5, 3, 3, 2]
    rating = RatingStructure(my_list)

    console_methods.print_console("It's initial chain. Add new elems")
    rating.print_chain()

    # test_drive(rating)

    while True:
        integer_input = console_methods.input_digit(False)
        rating.insert_node(integer_input)
        console_methods.print_console("Added new\n")
        rating.print_chain()
        quuu = console_methods.input_one_string("\nTo quiet enter q")
        if quuu.__eq__("q"):
            break
