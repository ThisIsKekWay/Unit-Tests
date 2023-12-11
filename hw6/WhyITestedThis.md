# Домашная работа №6

## Этап инициализации класса

В этом блоке тестировалось поведение инициализатора `__init__`. Тестирование этого блока необходимо для дальнейшей правильной работы остальных функций приложения. Тестирование учитывает типы данных, подаваемых инициализатору в качестве аргументов. В случае неверного типа данных пробрасывается исключение. Следующей проверкой данных является проверка типов внутри списка с пробросом исключения в случае неверного типа данных. В случае верных типов в списке происходит инициализация класса с сохранением списков чисел.

### Блок инициализатора

```
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
```

### Блок тестов
```
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

    def test_init_invalid_type_list_3(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = ["not an int", 2, 3]
        list_2 = [1, 2, 3]
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)

    def test_init_invalid_type_list_4(self):
        """ Инициализация списков с проверкой типа данных """
        list_1 = [1, 2, 3]
        list_2 = ["not an int", 2, 3]
        with pytest.raises(TypeError):
            ListCalculator(list_1, list_2)
```



## Блок расчета среднего

В данном блоке происходит проверка правильности расчета среднего арифметического. Благодаря предыдущему блоку мы уверены, что в эту функцию будут переданы только валидные значения. Тестирование этого блока необходимо для обеспечения правильности вычислений и работы блока сравнения.

### Блок среднего
```
def avg(self, listt):
        """ Среднее арифметическое списка"""
        return sum(listt) / len(listt)
```

### Блок тестов
```
def test_avg(self):
        """ Среднее арифметическое списка """
        list_1 = [1, 2, 3, 4, 5]
        list_2 = [1, 2, 3, 4, 5]
        calc = ListCalculator(list_1, list_2)
        result = calc.avg(list_1)
        assert result == 3
```

## Блок сравнения средний значений

В этом блоке сравниваются средние значения. Тестирование здесь необходимо для проверки выводов функции.

### Блок сравнения
```
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
```
### Блок тестов
```
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
```