"""
# author Liu shi hao
# date: 2019/11/15 16:36
# file_name: user

"""


class User:
    def __init__(self,password) -> None:
        super().__init__()
        self.__key = 666666
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value ^ self.__key
        pass

    def login(self, password):
        return self.password == password ^ self.__key


user1 = User(123456)
print(user1.password)
user_password = int(input("请输入密码："))
print(user1.login(user_password))

