"""
# author Liu shi hao
# date: 2019/11/19 14:44
# file_name: obj_test

"""
class Student:
    """
    这是学员类
    """

    def __init__(self,name,age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __eq__(self, o) -> bool:
        return self.name == o.name and self.age == o.age

    def __gt__(self, other):
        return self.age > other.age

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return f"学员名{self.name}年龄{self.age}"


#
# s1 = Student("001",21)
# s2 = Student("011",11)
# print(s1 ==s2)
# print(s1 > s2)
# print(s1 is s2)
# print(s1 != s2)
# print(s1)
# print(s2)
# print(s1.__doc__)
# print(__doc__)

class Animal:

    def eat(self):
        print("动物吃")



class Dog(Animal):
    def play(self):
        print("狗狗玩耍")


class Cat(Animal):
    def catch(self):
        print("猫捉老鼠")

def do_action(an):
    if type(an ) is Animal:
        an.eat()
    elif an.__class__ is Dog:
        an.play()
    else:
        an.catch()

do_action(Dog())
do_action(Cat())
do_action(Animal())
do_action(Cat())
do_action(Animal())
print(issubclass(Dog,Cat))
print(issubclass(Dog,Animal))
print(issubclass(Animal,Animal))


def feed(an):
    if issubclass(type(an) ,Animal):
        an.eat()
    else:
        print("养不起")

feed(Dog())
feed(Cat())
feed(Animal())
feed(Student("111",12))
print(dir(Dog()))


def show_obj(obj):
    if "type_name" in dir(obj):
        print(obj.type.name)
    if hasattr(obj,"play"):
        obj.play()
    if hasattr(obj,"catch"):
        obj.catch()
show_obj(Animal())
show_obj(Dog())
show_obj(Cat())































