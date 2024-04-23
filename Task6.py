"""
Изучить что такое множественное наследование и миксины,
привести пример использования данных концепций ООП
"""

"""
 Как я выяснил, миксины  это форма множественного наследования, 
 позволяют расширять функциональность классов без глубокой иерархии наследования.
 Миксины создаются для того, чтобы повторно использовать функции во множестве классов. 
 Они не предполагают создание объектов, и не должны иметь своего состояния.
"""

# пример множественного наследования и миксины
class A:
    def met_a(self):
        return "Метод A"

class B:
    def met_b(self):
        return "Метод B"

class C(A, B):
    def met_c(self):
        return "Метод С"

c = C()
print(c.met_a())
print(c.met_b())

# По сути A и B это миксины

