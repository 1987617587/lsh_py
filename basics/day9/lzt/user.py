# author:lzt
# date: 2019/11/15 16:35
# file_name: user
class User:

    def __init__(self,password) -> None:
        super().__init__()
        self.__key = 123456
        self.password = password


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value ^ self.__key
        pass

    def login(self,password):
        return self.__password == password ^ self.__key


user1 = User(223344)
print(user1.password)
# 验证密码
user_password = int(input("密码："))
# print(user_password == user1.password)
print(user1.login(user_password))


