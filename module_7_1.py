from pprint import pprint

__file_name = 'products.txt'
__file_name = open(__file_name, "r")

pprint(__file_name)


class Product():
    def __init__(self, name, weight, category):
        if not isinstance(name, str):
            raise TypeError("Название продукта должно быть строкой")
        self.name = name
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес продукта должен быть числом")
        self.weight = weight
        if not isinstance(category, str):
            raise TypeError("Категория продукта должно быть строкой")
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        with open(self.__file_name, "r") as file:
            products = file.read().strip().split('\n')
        return products
    def add(self, *products):
        with open(self.__file_name, "a") as file:
            for product in products:
                if str(product) not in self.get_products():
                        file.write(str(product) + "\n")
                else:
                    print(f"Продукт {product} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
