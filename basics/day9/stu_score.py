"""
# author Liu shi hao
# date: 2019/11/15 16:03
# file_name: stu_score

"""


class Stu:
    def __init__(self, name, score) -> None:
        super().__init__()
        self.name = name
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0 or value > 100:
            print("分数无效！")
            self.__score = 0
        else:
            self.__score = value
        # 数据之间的联动
        self.__s_pass = self.__score >= 60
        pass

    @property
    def s_pass(self):
        return self.__s_pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 6:
            print("名字的长度必须在3-5位之间")
        else:
            self.__name = value

        pass


s1 = Stu("123", -90)
print(s1.s_pass)
# s1.score = 40
# s1.name = "4678"
# print(s1.s_pass)
# print(s1.name)
