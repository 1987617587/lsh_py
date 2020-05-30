# author:lzt
# date: 2019/11/15 15:51
# file_name: stu_score
class Student:

    # name:学员名字
    # score:学员成绩
    # s_pass:是否通过
    def __init__(self, name, score) -> None:
        super().__init__()
        self.name = name
        self.score = score

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if len(value) < 6 or len(value) > 15:
            print("名字的长度必须在6-15位之间")
        else:
            self.__name = value
        pass

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0 or value > 100:
            print("分数无效")
            self.__score = 0
        else:
            self.__score = value
        # 数据之间联动
        self.__s_pass = self.__score >= 60
        pass

    @property
    def s_pass(self):
        return self.__s_pass


s1 = Student("123456",60)
s1.score = 59
print(s1.s_pass)


