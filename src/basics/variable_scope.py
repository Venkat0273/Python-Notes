# -*- coding: utf-8 -*-

__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def scope():
    num = 0
    def increment():
        nonlocal num
        num = num + 1
        return num
    return increment()


# print(scope())
x: str = "Bye"
def global_scope():
    global x
    x = "Hi"
    print(x)


# global_scope()

a = "global"


class Venkat(object):

    a = "class"
    b = "some"
    c = "some 2"
    d = "some 3"
    e = lambda : a
    f = lambda a = a : a

    @staticmethod
    def printing():
        return a


v = Venkat()
print(v.a)
print(v.printing())
print(v.f())
print(v.e)


