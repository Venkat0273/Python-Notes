# -*- coding: utf-8 -*-
__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def block_indentation():
    if 10 > 10:
        print("if statement indented")
    elif 10 > 5:
        print("elif statement indented")
    else:
        print("else default statement indented")

    for i in range(10):
        print(i)
        print("For loop also indented")

    a = 0
    while a > 2:
        print("While loop also indented with 4 spaces but not tab")
        print(a)
        a = a + 1


if __name__ == "__main__":
    block_indentation()
