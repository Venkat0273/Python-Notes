# -*- coding: utf-8 -*-

__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


from typing import ClassVar


class Object(object):
    """Simple comparison object class"""

    def __init__(self, x: int) -> None:
        self.item: int = x
    
    def __eq__(self, other: int) -> bool:
        return self.item == other
    
    def __ne__(self, other:int) -> bool:
        return self.item != other
    
    def __lt__(self, other: int) -> bool:
        return self.item < other
    
    def __gt__(self, other: int) -> bool:
        return self.item > other
    

obj = Object(2)
obj2 = Object(3)

print(obj == obj2)
print(obj != obj2)
print(obj < obj2)
print(obj > obj2)
