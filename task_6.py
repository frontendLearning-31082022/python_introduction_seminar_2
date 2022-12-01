# 6) *Реализовать структуру данных «Товары». Она должна представлять собой 
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами 
# (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные 
# у пользователя.
from console_methods import input_strings_while_q, input_one_string


# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, 
# в котором каждый ключ — характеристика товара, например название, 
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

class Products:
    # лучше хэшмап
    list = []

    temp_id = None
    temp_feature_name = None
    temp_feature = None

    temp_dict = {}

    def __add_product(self):
        dsf = 4

    def add_feature(self):
        self.temp_dict[self.temp_feature_name] = self.temp_feature

    def save_to_db(self):
        tuple_new = self.temp_id, self.temp_dict
        self.list.append(tuple_new)
        self.__clear_temp()

    def __clear_temp(self):
        self.temp_id = None
        self.temp_feature_name = None
        self.temp_feature = None

        self.temp_dict = {}

    def parse_features(self, name_n_val):
        two_vals = []
        for data in name_n_val:
            two_vals.append(data)
            if len(two_vals) == 2:
                products.temp_feature_name = two_vals[0]
                products.temp_feature = two_vals[1]
                two_vals.clear()
                products.add_feature()

    def input_by_test_driven(self, id, *name_n_val):
        products.temp_id = id
        self.__parse_features(name_n_val)
        products.save_to_db()

    def get_all_names_features(self):

        types_names = {}
        for product_item in self.list:
            names = dict(product_item[1]).keys()
            for name in names:
                types_names[name] = set()

        for product_item in self.list:
            for name_uniq in types_names:
                if dict(product_item[1]).__contains__(name_uniq):
                    set_vals = types_names[name_uniq]
                    set_vals.add(dict(product_item[1])[name_uniq])

        result = str(types_names).replace("{", "[").replace("}", "]")
        result = result[1:len(result) - 1].replace("],", "],\n")
        self.__clear_temp()
        return "{\n " + result + "\n}";


def make_tuple_per_item(id, features):
    return (id, features)


def input_data_test_driven():
    products.input_by_test_driven(1, 'name', 'computer', 'price', 20000,
                                  'count', 5, 'type_item', 'psc.')
    products.input_by_test_driven(2, 'name', 'printer', 'price', 6000,
                                  'count', 2, 'type_item', 'psc.')
    products.input_by_test_driven(3, 'name', 'scanner', 'price', 2000,
                                  'count', 7, 'type_item', 'psc.')


if __name__ == '__main__':
    products = Products()
    # input_data_test_driven()

    while True:
        id = input_one_string("Input id item")
        products.temp_id = id

        inputed_fe_na = input_strings_while_q("Input name and feature line "
                                              "by line (enter push)")
        products.parse_features(inputed_fe_na)
        products.save_to_db()
        req_quiet = input_one_string("finish input? Input q")
        if req_quiet.__eq__("q"):
            break

    msg_result = products.get_all_names_features()
    print(msg_result)
