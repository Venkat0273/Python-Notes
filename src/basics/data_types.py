# -*- coding: utf-8 -*-
__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def data_type():
    # bool data type
    a: bool = True
    b: bool = False
    print(isinstance(a, bool))
    print(isinstance(b, bool))
    print(issubclass(bool, int))
    print(isinstance(a, int))
    print(a * b)
    print(a + b)
    print(a * a)
    
    # number data types
    a: int = 2343243
    b: float = 3.1434
    c: complex = 3+4j
    print(isinstance(a, int))
    print(isinstance(b, float))
    print(isinstance(c, complex))

    print(a + a, a - a, a * a, a / a, a // a, a % a)
    print(b + b, b - b, b * b, b / b, b // b, b % b)
    try:
        print(c + c, c - c, c * c, c / c)
    except TypeError as e:
        print(e.__str__())
        print(e.args)
        print(e.__dict__)
        print(e.__repr__())

    # string data type

    a: str = "venkatarami reddy"
    c: bytes = b"venkatarami reddy"
    print(isinstance(a, str))
    print(isinstance(c, bytes))

    # Sequences and Collections

    # Ordered Sequences
    a: str = "venkat"
    b: list = [1, 2, 3, 4]
    d: tuple = (1, 2, 3, 4)
    print(f"{a} is {isinstance(a, str)}")
    print(f"{b} is {isinstance(b, list)}")
    print(f"{d} is {isinstance(d, tuple)}")

    # Unordered Collections
    a: set = {1, 2, 3, 4}
    b: dict = {"a": "venky", "b": "venkat"}

    print(f"{a} is {isinstance(a, set)}")
    print(f"{b} is {isinstance(b, dict)}")


if __name__ == "__main__":
    data_type()
