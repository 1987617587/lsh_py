# 用装饰器装饰类:
from typing import Any
from functools import wraps


def single(cls):
    @wraps(cls)
    def wrapper(*args):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.__init__(cls._instance, *args)
        return cls._instance

    return wrapper


# 用装饰器让类变成单例类
@single
class Singleton:
    _instance = None

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age


s1 = Singleton("张三", 19)
s2 = Singleton("李四", 20)
print(id(s1), id(s2))
print(s1.name)
print(s2.name)
print(s1.age)


