class Calculator:
    def calculation(self, x: int, y: int, op: str):
        result: int
        if type(x) is int and type(y) is int:
            if op in "+-*/":
                if op == "+":
                    return x + y
                elif op == "-":
                    return x - y
                elif op == "*":
                    return x * y
                elif op == "/":
                    if y == 0:
                        raise ZeroDivisionError
                    else:
                        return x / y
            else:
                raise ValueError("Invalid operator")
        else:
            raise TypeError("Invalid data type")

    def squareRoot(self, x):
        if type(x) is int:
            if x >= 0:
                t: float = 0
                squareroot: float = x / 2
                while (t - squareroot) != 0:
                    t = squareroot
                    squareroot = (squareroot + (x / squareroot)) / 2
                return squareroot
            else:
                raise ValueError("Invalid number")
        else:
            raise TypeError("Invalid data type")

    def calculating_discount(self, purchase_amount: int, discount_amount: int) -> float:
        if type(purchase_amount) is int and type(discount_amount) is int:
            if 0 > discount_amount or discount_amount > 100:
                raise ValueError("Invalid discount amount")
            else:
                if purchase_amount < 0:
                    raise ValueError("Invalid purchase amount")
                else:
                    return purchase_amount - discount_amount * purchase_amount / 100
        else:
            raise TypeError("Invalid data type")
