"""
# author Liu shi hao
# date: 2019/11/21 15:50
# file_name: recu_test
了解深度递归
"""
class Person:
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self.__name  # 注意用下划线区分，避免深度递归

    @name.setter
    def name(self, value):
        self.__name = value
        pass

p1 = Person("1")