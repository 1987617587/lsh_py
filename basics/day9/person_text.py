"""
# author Liu shi hao
# date: 2019/11/15 15:23
# file_name: person_text

"""


class Person:

    def __init__(self, gender) -> None:
        super().__init__()
        self.set_gender(gender)

    def set_gender(self, gender):
        if gender == "男" or gender == "女":
            self.__gender = gender
        else:
            print("性别异常，已设定默认值！")
            self.__gender = "男"

    def get_gender(self):
        return self.__gender


# p1 = Person("&")
# print(p1.get_gender())
# p1.set_gender("妖")
# print(p1.get_gender())
# p1.set_gender("女")
# print(p1.get_gender())


class Dog:

    def __init__(self, name, sex) -> None:
        super().__init__()
        self.name = name
        self.sex = sex

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value == "公" or value == "母":
            self.__sex = value
        else:
            print("性别异常 已设定默认值！")
            self.__sex = "母"
        pass


dog1 = Dog("asd", "sd")
print(dog1.sex)
dog1.sex = "公"
print(dog1.sex)
