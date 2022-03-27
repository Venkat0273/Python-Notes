# -*- coding: utf-8 -*-
__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def type_casting() -> None:
    # One data type can be converted into another data type
    # This process is called type casting
    # Below are the examples of type casting
    # True, False, None, NotImplemented are the built-in constants
    a: int = 2343
    b: float = 23.423
    c: str = "venkat"
    d: list = [2, 3, 4]
    e: tuple = (3, 3, 3)
    f: set = {2, 3, 4}
    g: dict = {"a":"venkat"}
    print(float(a))
    print(int(b))
    print(list(c))
    print(tuple(c))
    print(set(c))


if __name__ == "__main__":
    type_casting()
