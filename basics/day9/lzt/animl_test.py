# author:lzt
# date: 2019/11/15 17:42
# file_name: animl_test
class Animal:

    def __init__(self, name, type, height, weight) -> None:
        super().__init__()
        self._name = name
        self.type = type
        self.height = height
        self.weight = weight

    def eat(self):
        print("动物吃")


class Dog(Animal):

    def __init__(self, name, type, height, weight, food) -> None:
        super().__init__(name, type, height, weight)
        self.food = food


# 测试Dog中的内容
dog1 = Dog("旺财", "犬科", 1, 50, "大骨头")
print(dog1._name)
print(dog1.food)
dog1.eat()
