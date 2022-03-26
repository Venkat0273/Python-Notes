# -*- coding: utf-8 -*-
__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def variables():
    a = 123;
    b = 234234234234234234324;
    c = 3.14
    d = "venkat"
    e = 3+4j
    f = True
    # Checking the types of variables
    print(f"{a} is of type {type(a)}")
    print(f"{b} is of type {type(b)}")
    print(f"{c} is of type {type(c)}")
    print(f"{d} is of type {type(d)}")
    print(f"{e} is of type {type(e)}")
    print(f"{f} is of type {type(f)}")
    # Checking the instances of the variables

    print(f"{a} is instance of int {isinstance(a, int)}")
    print(f"{b} is instance of int {isinstance(b, int)}")
    print(f"{c} is instance of float {isinstance(c, float)}")
    print(f"{d} is instance of str {isinstance(d, str)}")
    print(f"{e} is instance of complex {isinstance(e, complex)}")
    print(f"{f} is instance of bool {isinstance(f, bool)}")

    # Assignment errors
    # All errors
    try:
        a,b,c = 1, 2, 3
        a, b = 1, 2, 3
    except ValueError as e:
        print(e.__dir__())
        print(e.__dict__)
        print(e.__context__)
        print(e.args)
        print(e.__cause__)
        print(e.__repr__())
        print(e.__str__())

    # Can also be assigned as shown below
    x = y = z = 2
    


if __name__ == "__main__":
    variables()
