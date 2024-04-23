"""
 Создать класс для геометрической фигуры на выбор и
 добавить в него два метода – первый для расчета площади,
 второй для расчета периметра
"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def area(self):
        area = self.a * self.b
        return area

    def perimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter


rectangle = Rectangle(4, 6)
print(f"Площадь = {rectangle.area()}")
print(f"Периметр = {rectangle.perimeter()}")