""" Тесты """
import pytest
from main import ListCalculator


class TestListCalculator:
    """ Тесты для ListCalculator """

    def test_init_valid_lists(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = [1, 2, 3]
        list_2 = [4, 5, 6]
        calc = ListCalculator(list_1, list_2)
        assert calc.list_1 == list_1
        assert calc.list_2 == list_2

    def test_init_empty_list_1(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = []
        list_2 = [4, 5, 6]
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)

    def test_init_empty_list_2(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = [1, 2, 3]
        list_2 = []
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)

    def test_init_invalid_type_list_1(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = "not a list"
        list_2 = [4, 5, 6]
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)

    def test_init_invalid_type_list_2(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = [1, 2, 3]
        list_2 = "not a list"
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)

    def test_avg(self):
        """ Среднее арифметическое списка """
        list_1 = [1, 2, 3, 4, 5]
        list_2 = [1, 2, 3, 4, 5]
        calc = ListCalculator(list_1, list_2)
        result = calc.avg(list_1)
        assert result == 3

    def test_avg_comparison_greater(self):
        """ Сравнение средних значений списков """
        list_1 = [1, 2, 3]
        list_2 = [4, 5, 6]
        calc = ListCalculator(list_1, list_2)
        result = calc.avg_comparison()
        assert result == "Второй список имеет большее среднее значение"

    def test_avg_comparison_lesser(self):
        """ Сравнение средних значений списков """
        list_1 = [4, 5, 6]
        list_2 = [1, 2, 3]
        calc = ListCalculator(list_1, list_2)
        result = calc.avg_comparison()
        assert result == "Первый список имеет большее среднее значение"

    def test_avg_comparison_equal(self):
        """ Сравнение средних значений списков """
        list_1 = [1, 2, 3]
        list_2 = [3, 2, 1]
        calc = ListCalculator(list_1, list_2)
        result = calc.avg_comparison()
        assert result == "Средние значения равны"
