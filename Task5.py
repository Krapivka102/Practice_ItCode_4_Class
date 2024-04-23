"""
Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
В базовый класс добавить get_paid(), который в дальнейшем переопределить в дочерних,
чтобы сотрудники разных должностей получали различную зарплату
"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_paid(self):
        print("Пока что я ничего не делаю")


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    # у менеджера будет фиксированная зарплата
    def get_paid(self):
        return self.salary


class Worker(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours

    # у рабочего будет считаться как за отработанные часы, то есть rate это ставка в час в hours отработанные часы
    def get_paid(self):
        return self.rate * self.hours


manager = Manager("Олег", 60000)
worker = Worker("Никита", 210, 35)

print(f"Зарплата менеджера: {manager.get_paid()}")
print(f"Зарплата работника: {worker.get_paid()}")