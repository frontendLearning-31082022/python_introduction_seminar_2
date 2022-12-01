# Реализуйте алгоритм перемешивания списка.
import random

if __name__ == '__main__':

    list_shuffle = []

    for value in range(1, 100):
        list_shuffle.append(value)

    for value in list_shuffle:
        random_pos = random.randint(0, len(list_shuffle) - 1)
        temp_val = value
        value = list_shuffle[random_pos]
        list_shuffle[random_pos] = temp_val

    print(list_shuffle)
