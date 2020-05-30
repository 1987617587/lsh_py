# author:lzt
# date: 2019/11/15 17:15
# file_name: role
class RoleSuper:
    pass
class Role(RoleSuper):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
        self.__hp = 1500
        self.__atk = 1000
        self.__level = 1
        self.__state = True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(str(value)) < 6 or len(value) > 15:
            print("名字长度:6-15")
            return
        self.__name = value
        pass

    @property
    def hp(self):
        return self.__hp

    @property
    def level(self):
        return self.__level

    @property
    def atk(self):
        return self.__atk

    # 成员方法中
    def up_level(self):
        self.__hp += 100
        self.__atk += 50
        self.__level += 1


