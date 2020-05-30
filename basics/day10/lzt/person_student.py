# author:lzt
# date: 2019/11/18 14:17
# file_name: person_student
class Person:
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃的五花八门")


class Student(Person):
    def __init__(self, name, age, score) -> None:
        # 初始化父亲的成员变量
        super().__init__(name, age)
        # 子类中若声明和父亲同名的成员变量:为父亲的成员变量做修改 并未追加新的成员变量
        self.name = "学生xxx"
        # 为子类追加独有的成员变量
        self.score = score

    def eat(self):
        print(f"{self.name}吃学生餐！")
        # 调用父类被覆盖的方法
        # super().eat()


s1 = Student("001", 19, 99)
s1.eat()
