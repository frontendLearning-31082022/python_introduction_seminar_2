# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

if __name__ == '__main__':
    print("Input several words by space character separator")
    inputed = input()
    array_words = inputed.split(" ")

    max_characters_in_word = 10
    iter = 1
    for word_item in array_words:
        print(str(iter) + " " + word_item[0:max_characters_in_word])
        iter += 1
