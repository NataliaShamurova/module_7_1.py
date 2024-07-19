
from pprint import pprint
class Product:

    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():

    def __init__(self):
        self.__file_name = '7_1.txt'

    
    def get_products(self):

        file = open(self.__file_name, 'r')
        file_contents = file.read()
        #file.close()
        return file_contents
        file.close()


    def add(self, *products):
        for i in products:
            self.opener = open(self.__file_name, 'r')
            if i.name not in self.opener.read():
                self.opener = open(self.__file_name, 'a')
                self.opener.writelines(f'{i}\n')
                self.opener.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине.')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('wer', 5.5, 'Vegetables')
p5 = Product('fvc', 5.5, 'Vegetables')

#print(p1)
print(p2)  # __str__
#print(p3)


s1.add(p1, p2, p3, p4, p5)

print(s1.get_products())
f = open('7_1.txt', 'r')
print('1', f.read())
print('2', f.read())