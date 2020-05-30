"""
# author Liu shi hao
# date: 2019/12/11 9:46
# file_name: test
用装饰器装饰类（单例模式）
"""

from functools import wraps


def single(cls):
    @wraps(cls)
    def wrapper(*args):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.__init__(cls._instance, *args)
        return cls._instance

    return wrapper


from typing import Any


@single
class Singleton:
    _instance = None

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


s1 = Singleton("ni")
s2 = Singleton("no")
print(id(s1), id(s2))
print(s1.name, s2.name)
