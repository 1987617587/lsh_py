# author:lzt
# date: 2019/11/20 15:44
# file_name: single_test
from typing import Any


class Book:

    def __new__(cls, name) -> Any:
        print("类的构造执行了 对象就会出生")
        return super().__new__(cls)

    def __init__(self, name) -> None:
        super().__init__()
        print("初始化方法执行了")
        self.name = name

    def __str__(self) -> str:
        return self.name


class Book_DB:
    """
    书籍的存储类：书的仓库
    """
    _instance = None
    _flag = False

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not Book_DB._flag:
            super().__init__()
            self.__books = []
            Book_DB._flag = True

    # books = []:存储书籍的列表 不推荐使用类变量

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        for i in range(len(self.__books)):
            print(self.__books[i])


book_db = Book_DB()
book_db.add_book(Book("红与黑"))

# 若此时有另外的程序也需要书籍仓库
book_db2 = Book_DB()
book_db2.add_book(Book("编程从精通到放弃"))

# book_db.show_books()
book_db2.show_books()


class OnlyObjClass:
    # 设定一个类变量 用于保存唯一实例的地址 也为了监视是否已产生过对象
    _instance = None
    # 类变量:初始化标识
    _init_flag = False

    def __new__(cls, name) -> Any:
        # 构造中判断监视变量是否已经指向一个对象：
        if cls._instance is None:
            # 未保存任何对象
            cls._instance = super().__new__(cls)
        # 已经有对象
        return cls._instance

    def __init__(self, name) -> None:
        if not OnlyObjClass._init_flag:
            super().__init__()
            print("初始化对象")
            self.name = name
            OnlyObjClass._init_flag = True


# o1 = OnlyObjClass("张三")
# o2 = OnlyObjClass(None)
# print(id(o1), id(o2))
# o2.name = "李四"
# print(o1.name)
# print(o2.name)
