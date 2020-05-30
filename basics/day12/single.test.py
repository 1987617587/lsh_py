"""
# author Liu shi hao
# date: 2019/11/20 15:49
# file_name: single.test

"""
from typing import Any


class Book:
    def __new__(cls, name) -> Any:
        print("类的构造开始执行 ，对象出生")
        return super().__new__(cls)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        print("初始化方法执行了")

    def __str__(self):
        return self.name


class BookDb:
    _instance = None
    _init_flag = False

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not BookDb._init_flag:
            super().__init__()
            self.__books = []
            BookDb._init_flag = True

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        for i in range(len(self.__books)):
            print(self.__books[i])


book_db = BookDb()
book_db.add_book(Book("红与黑"))

# 若此时有另外的程序也需要书籍仓库
book_db2 = BookDb()
book_db2.add_book(Book("编程从精通到放弃"))

# book_db.show_books()
book_db2.show_books()


class OnlyObjClass:
    _instance = None
    _init_flag = False

    def __new__(cls, name) -> Any:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name) -> None:
        if not OnlyObjClass._init_flag:
            super().__init__()
            self.name = name
            OnlyObjClass._init_flag = True

# OnlyObjClass("1")
# print(id(OnlyObjClass))
# o1 = OnlyObjClass("1")
# o2 = OnlyObjClass("2")
# print(id(o1),id(o2))
# print(o1.name)
# print(o2.name)
# o1.name = 2
# print(o1.name)
# print(o2.name)
