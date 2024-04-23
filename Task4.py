"""
 Изучить метод  __str__, создать класс с данным методом, продемонстрировать его выполнение
"""

"""
 Как я выяснил метод __str__ должен возвращать строку, 
 которая будет использоваться при попытке преобразовать объект в строку с помощью функции str() 
 или при попытке вывести объект с помощью функции print().
"""

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя клиента = {self.name}, Возраст клиента = {self.age}"


customer = Customer('Никита', 21)
print(str(customer))
print(customer)