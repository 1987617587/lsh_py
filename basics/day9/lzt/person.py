# author:lzt
# date: 2019/11/15 15:11
# file_name: person
class Person:

    def __init__(self, name,gender) -> None:
        super().__init__()
        # self.__genger = gender
        self.name = name
        self.gender = gender
        # self.set_gender(gender)

    # def set_gender(self, gender):
    #     if gender == "男" or gender == "女":
    #         self.__genger = gender
    #     else:
    #         print("性别异常 已设定默认值!")
    #         self.__genger = "男"
    #
    # def get_gender(self):
    #     return self.__genger

    # @property
    # def gender(self):
    #     return self.__gender

    # 代表了get_gender这个方法
    @property
    def gender(self):
        return self.__gender

    # 代表了set_gender(self,gender)
    # value是获取外部传入的实参的形参
    @gender.setter
    def gender(self, value):
        if value == "男" or value == "女":
            self.__gender = value
        else:
            print("性别异常 设定默认值！")
            self.__gender = "男"
        pass


p1 = Person("","?")
# print(p1.__genger)
# print(p1.get_gender())
# # p1.set_gender("妖")
# # print(p1.get_gender())
# 属性的访问类似于成员变量的访问方式
p1.gender = "妖"
print(p1.gender)
#
# 主要用于快速构建代码：
# prop+回车：生成只读属性
# props+回车：生成可读写属性
# propsd+回车：生成可读写删属性