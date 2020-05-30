"""
# author Liu shi hao
# date: 2019/11/21 10:56
# file_name: object_test

"""
class Student:
    pass

s1 = Student()
s1.name = "asdf"
s1.age = 19
s2 = Student()
s2.name = "a111"
print(s1.name)

def show_info(self):
    print(f"{self.name}被动态追加了")



Student.show = show_info

# s1.show(s1)
s1.show()
s2.show()

@classmethod
def class_method(cls):
    print(cls)

Student.clm = class_method
Student.clm()

Student.count = 0
print(s1.count)

@staticmethod
def static_method():
    print("静态函数追加")

Student.sta = static_method
Student.sta()

del Student.clm
# Student.clm()
del Student.sta
# Student.sta()
del s1
# print(s1.name)
print(dir(Student))
print(dir(s2))