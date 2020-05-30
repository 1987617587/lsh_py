"""
# author Liu shi hao
# date: 2019/11/15 17:49
# file_name: animl

"""
class Animal:

    def __init__(self,name,type,height,weight) -> None:
        super().__init__()
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight

    def eat(self):
        print("开饭了！")



class Dog(Animal):


    def __init__(self, name, type, height, weight,age) -> None:
        super().__init__(name, type, height, weight)
        self.age = age

    def eat(self):
        print("狗改不了吃屎！")


dog1 = Dog("旺财","犬科",1,58,4)
print(dog1.name)
dog1.eat()








