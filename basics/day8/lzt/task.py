# author:lzt
# date: 2019/11/15 9:26
# file_name: task
# 1.尝试写一个学员类，想一想都应该有些什么变量和方法，
# 并产生5个对象来表示你自己及身边的四位同学吧，
# 你觉得程序中的对象和你们是什么关系？学员类和你们又是什么关系？
class Student:
    # 学生有啥?
    def __init__(self, name, age, num, gender, addr, h, w) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.num = num
        self.gender = gender
        self.addr = addr
        self.h = h
        self.w = w

    # 学生能干啥?
    def study(self):
        print(f"{self.name}在学习")


# s1 = Student("张晨鑫", 18, "001", "男", "山西忻州", 1.7, 60)
# s2 = Student("胡亚豪", 18, "001", "男", "山西忻州", 1.7, 60)
# s3 = Student("张晨鑫1", 18, "001", "男", "山西忻州", 1.7, 60)
# s4 = Student("张晨鑫2", 18, "001", "男", "山西忻州", 1.7, 60)
# s5 = Student("张晨鑫3", 18, "001", "男", "山西忻州", 1.7, 60)
#
# 2.员工类：属性：名字、工号、部门、工资 方法：涨工资
class Emp:

    def __init__(self, name, num, dp, salary) -> None:
        super().__init__()
        self.name = name
        self.num = num
        self.dp = dp
        self.salary = salary
        pass

    # 涨工资
    def raise_salary(self, money):
        print("涨了！")
        self.salary += money


# emp1 = Emp("001","007","研发部",12000)
# print(f"{emp1.name}的薪资是{emp1.salary}")
# emp1.raise_salary(1500)
# print(f"{emp1.name}新的薪资是{emp1.salary}")

#
# 3.电脑类：属性：牌子，主板，cpu，内存，显示器，显卡等，方法：运行
class Computer:

    def __init__(self, sign, mb, cpu, memory, viwer, display_card) -> None:
        super().__init__()
        self.sign = sign
        self.mb = mb
        self.cpu = cpu
        self.memory = memory
        self.viwer = viwer
        self.display_card = display_card

    def run(self):
        print(f"{self.mb}加电")
        print(f"{self.cpu}运算")
        print(f"{self.memory}载入数据")
        print(f"{self.display_card}载入数据")
        print(f"{self.viwer}显示数据")
        print(f"{self.sign}运行了")


# com1 = Computer("宇宙一号", "技嘉", "i9", "金邦", "LG", "1080")
# com1.run()

#
# 4.设计一个游戏角色类
#    属性:角色名、血量、魔法、状态
#    方法:释放技能 被伤害
#    要求:设计要合理
class Role:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.hp = 1000
        self.mp = 350
        # True:活着 False:挂了
        self.state = True

    def release(self, sk_mp):
        # 当前玩家的状态检测
        if self.state:
            # 判断魔法值是否足够
            if self.mp >= sk_mp:
                self.mp -= sk_mp
                print("技能释放成功！")
                return
            print("技能无法释放！")
        else:
            print("请先复活！")

    def be_hurt(self, hurt):
        # 检测当前玩家的状态
        if self.state:
            # 减掉当前玩家的血量值
            self.hp -= hurt
            if self.hp <= 0:
                self.hp = 0
                # 状态同步
                self.state = False
            print(f"当前玩家的血量值:{self.hp}")
        else:
            print("请尊重死者！")


# role1 = Role("123")
# role1.be_hurt(500)
# role1.be_hurt(500)
# role1.be_hurt(500)
# role1.release(150)
# role1.release(150)
# role1.release(150)
# role1.release(150)
# role1.release(150)
#
# 5.Lader类具有类型为浮点数的上底、下底、高、面积属性，具有返回面积的功能，
# 包括一个初始化方法对上底、下底、高进行初始化。Circle类具有类型为浮点型的半径、周长和面积属性，
# 具有返回周长、面积的两个方法，包括一个初始化方法对半径进行初始化。测试类Lader和类Circle的功能。
class Lader:

    def __init__(self, up, down, h) -> None:
        super().__init__()
        self.up = up
        self.down = down
        self.h = h

    def area(self):
        return (self.up + self.down) * self.h / 2


# lader1 = Lader(1, 2, 3)
# print(lader1.area())
#
# 6.定义一个人类Person：
# 1)定义一个方法say_hello()，可以向对方发出问候语“hello,my name is XXX”
# 2)有三个属性：名字、身高、体重
# 3)通过初始化方法，分别给三个属性赋值
# 4)测试:
# 1、创建两个对象，分别是zhangsan，1.73，55；lishi，1.80，65
# 2、分别调用对象的say_hello()方法。
class Person:

    def __init__(self, name, h, w) -> None:
        super().__init__()
        self.name = name
        self.h = h
        self.w = w

    def say_hello(self):
        print(f"hello,my name is {self.name}")


# p1 = Person("zhangsan",1.73,55)
# p2 = Person("lisi",1.80,65)
# p1.say_hello()
# p2.say_hello()
#
# 7.
# 定义一个矩形类Rectangle：
# 1)定义三个方法：get_area()求面积、get_per()求周长，show_all()输出长、宽、面积、周长。
# 2)有2个属性：长length、宽width
# 3)通过初始化方法分别给两个属性赋值
class Rectangle:

    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_per(self):
        return 2 * (self.width + self.height)

    def show_all(self):
        return f"长{self.width} 宽{self.height} 面积{self.get_area()} 周长{self.get_per()}"


# rec1 = Rectangle(1,2)
# rec2 = Rectangle(2,3)
# rec3 = Rectangle(3,4)
# print(rec1.show_all())
# print(rec2.show_all())
# print(rec3.show_all())
#
#
# 8.
# 定义一个普通用户类
# 普通用户类具备的属性：用户名、密码、权限
# 普通用户类具备的方法：登录、注册
#
# 注意：请详细测试该类
# 对象列表
# 数据库对应的对象列表
# [1,2,3,4]
# ["1","3"]
# 对象放入列表
class User:

    def __init__(self, user_name, password, pri) -> None:
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.pri = pri

    def login(self, user_name, password):
        return self.user_name == user_name and self.password == password

    def register(self, user_name, password, pri):
        self.user_name = user_name
        self.password = password
        self.pri = pri


# 准备数据库中的对象列表
users = \
    [
        User("admin", "123", "admin"),
        User("user1", "123", "user"),
        User("user2", "123", "user"),
        User("user3", "123", "user"),
        User("g1", "123", "guest"),
    ]
# 模拟前端验证
# 登录的效果
# for j in range(3):
#     user_name = input("用户名:")
#     password = input("密  码:")
#     # 去挨个匹配数据库中的对象 是否有对象匹配上
#     # 保持登录用户的变量
#     login_user = None
#     for i in range(len(users)):
#         if users[i].login(user_name,password):
#             print("登录成功")
#             login_user = users[i]
#             break
#     else:
#         print("用户名或密码错误！" if j != 2 else "24小时内无法再次登录！")
#
#     if login_user is not None:
#         break

# 模拟前端的注册
# 注册的效果
# 问用户要信息
register_user = User(None, None, None)
user_name = input("注册用户名:")
while 1:
    password = input("注册密码:")
    re_password = input("重复密码:")
    if password != re_password:
        print("两次输入不一致 请重新输入！")
        continue
    break
# 产生用户对象
register_user.register(user_name, password, "admin")
# 对象存入数据库
users.append(register_user)

# 遍历数据库 验证是否注册完毕
for i in range(len(users)):
    print(f"用户名:{users[i].user_name} 密码:{users[i].password} 权限:{users[i].pri}")
