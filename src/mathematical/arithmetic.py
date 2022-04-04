# -*- coding: utf-8 -*-

__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"

import operator
import math


a, b = 1, 2

print(operator.add(a, b), a + b, sep="\t")
print(operator.sub(a, b), a - b, sep="\t")
print(operator.mul(a, b), a * b, sep="\t")
print(operator.truediv(a, b), a / b, sep="\t")
print(operator.floordiv(a, b), a // b, sep="\t")
print(divmod(a, b), a % b, sep="\t")
print(math.sqrt(2))
print(math.pow(2, 1/2))
print(math.exp(2))
print(math.log(10, 10))
print(2 ** (1/2))