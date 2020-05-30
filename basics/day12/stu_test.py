"""
# author Liu shi hao
# date: 2019/11/20 14:26
# file_name: stu_test

"""


class Student:
    teacher = "lzt"
    count = 0

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        Student.count += 1


s1 = Student("001")
s2 = Student("002")
s3 = Student("002")
# print(s1.teacher,s2.teacher)
# Student.teacher = "zzy"
# print(s1.teacher,s2.teacher)
# s1.teacher = "zs"
# print(s1.teacher,s2.teacher)
# print(Student.teacher)
#
# print(s1.count)
print(Student.count)


# Student.count = 1
# print(Student.count)
# def show():
#     print("show info")
#     pass
# s1.info = show()
# s1.info()

class WebSystem:
    _online_count = 0

    @classmethod
    def modify_online_count(cls, num):
        if type(num) == int:
            cls._online_count = num

    @classmethod
    def show_count(cls):
        print(cls._online_count)


WebSystem.modify_online_count(100)
WebSystem.show_count()
