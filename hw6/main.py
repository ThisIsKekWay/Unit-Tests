""" Создайте программу на Python или Java, которая принимает два списка
чисел и выполняет следующие действия:
    a. Рассчитывает среднее значение каждого списка.
    b. Сравнивает эти средние значения и выводит соответствующее сообщение:
""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
""Средние значения равны"", если средние значения списков равны."""


class ListCalculator:
    """ Класс для обработки списков"""

    def __init__(self, list_1: list[int | float], list_2: list[int | float]):
        """ Инициализация списков с проверкой типа данных"""
        if not isinstance(list_1, list) or not list_1:
            raise TypeError("Invalid data type")
        if not isinstance(list_2, list) or not list_2:
            raise TypeError("Invalid data type")
        for i in list_1:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("Invalid data type")
        for i in list_2:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("Invalid data type")
        self.list_1 = list_1
        self.list_2 = list_2

    def avg(self, listt):
        """ Среднее арифметическое списка"""
        return sum(listt) / len(listt)

    def avg_comparison(self):
        """ Сравнение средних значений списков"""
        avg1 = self.avg(self.list_1)
        avg2 = self.avg(self.list_2)
        if avg1 > avg2:
            res = "Первый список имеет большее среднее значение"
        if avg1 < avg2:
            res = "Второй список имеет большее среднее значение"
        if avg1 == avg2:
            res = "Средние значения равны"
        return res
