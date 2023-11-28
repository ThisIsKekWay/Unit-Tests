def number_interval(num: int | float) -> bool:
    if type(num) is int or type(num) is float:
        if 25 < num < 100:
            return True
        else:
            return False
    else:
        raise TypeError("Invalid data type")
