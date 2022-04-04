# -*- coding: utf-8 -*-

__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"

# set_one: set = {1, 2, 3, 4}
# set_two: set = {4, 5, 6, 7}

# print(set_one.union(set_two))
# print(set_one.difference(set_two))
# print(set_one.symmetric_difference(set_two))
# print(set_one.intersection(set_two))
# print(set_one.issuperset(set_two))
# print(set_one.issubset(set_two))
# print(set_one.isdisjoint(set_two))

from collections import Counter

values = [1, 2, 3, 4, 4, 4, 5, 5, 5, 2, 1, 3]
counter = Counter(values)

print(counter)
print(type(counter))
print(isinstance(counter, dict))
print(counter.__class__.__name__)
print(counter.__doc__)