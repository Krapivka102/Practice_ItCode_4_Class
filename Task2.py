"""
Создать класс Человек с полями: имя, город проживания и год рождения.
Написать метод, который будет возвращать возраст человека в годах
"""
from datetime import datetime

class Human:
    def __init__(self, name, city, year):
        self.name = name
        self.city = city
        self.year = year

    def get_age(self):
        age = 2024 - self.year
        return age

    # Если программу запускать не в этом году, то будет не верно, есть такое решение:
    def get_age_now(self):
        data = datetime.now()
        age = data.year - self.year
        return age


human = Human('Никита', 'Уфа', 2002)
print(f'Возраст {human.name} = {human.get_age()}')
