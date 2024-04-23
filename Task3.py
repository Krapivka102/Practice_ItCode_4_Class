"""
Создать класс калькулятор и описать в нём методы
для базовых математических операций для двух чисел
"""

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def split(self):
        if self.b == 0:
            return 'Деление на 0 невозможно!'
        else:
            return self.a // self.b

    def squared(self):
        return self.a ** self.b

calcut = Calculator(8, 4)
print(f'Плюс = {calcut.plus()}')
print(f'Минус = {calcut.minus()}')
print(f'Умножить = {calcut.multiply()}')
print(f'Разделить = {calcut.split()}')
print(f'В квадрат = {calcut.squared()}')