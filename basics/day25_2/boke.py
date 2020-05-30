"""
# author Liu shi hao
# date: 2019/12/6 21:27
# file_name: boke

"""


# 模拟简单的博客
# 1.账号注册，登陆验证
# 2.写文章，包含【标题，作者，时间，内容】
# 3.查询文章，列出所有文章及时间
# 4.可查看其中一篇文章
# 5.删除文章
# 6.修改文章
# 7.退出系统
#
#
#
# 模拟学生成绩管理系统
# 1.账号注册，登陆验证，班级管理
# 2.填写学员信息 和 成绩
# 3.查询所有学员成绩
# 4.查询其中一位成绩
# 5.修改学员成绩
# 6.删除学员
# 7.排序显示
# 8.退出系统
class StudentSystem:

    def __init__(self) -> None:
        super().__init__()
        self.__students = stus
        self.__login = None

    def create_account(self):
        print("欢迎进入学生成绩管理系统！")
        name = input("请输入您的真实姓名:")
        stu_num = input("请输入您的学号:")
        gender = input("请输入您的性别:")
        while True:
            pwd1 = input("请输入要设定的密码:")
            re_pwd = input("请重复输入要设定的密码:")
            if pwd1 == re_pwd:
                break
            else:
                print("两次密码输入不一致，请重设密码！")
        print("注册成功！")
        self.__login = Student(name, gender, stu_num, score=None, password=pwd1)
        self.__students.append(self.__login)

    def student_login(self):
        # 检测是否已登录
        if self.__login is not None:
            print("请勿重复登录！")
            return
        for j in range(3):
            stu_num = input("请输入学号:")
            pwd = input("请输入密码:")
            # 遍历所有的账户
            for i in range(len(self.__students)):
                if self.__students[i].stu_num == stu_num and self.__students[i].password == pwd:
                    self.__login = self.__students[i]
                    print("登录成功!")
                    return
            else:
                if j == 2:
                    print("您已被禁止登录，请联系教务处人员！")
                    return
                print(f"你输入的学号或密码有误，还有{2 - j}次登录机会")


class Student:

    def __init__(self, name, gender, stu_num, score, password) -> None:
        super().__init__()
        self.stu_num = stu_num
        self.gender = gender
        self.name = name
        self.score = score
        self.password = password

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __str__(self) -> str:
        return f"姓名{self.name}\t性别{self.gender}\t学号{self.stu_num}\t成绩{self.score}"


stus = [
    Student("sfs", "男", "001", 23, "124124"),
    Student("fsg", "男", "002", 22, "128724"),
    Student("ret", "女", "003", 92, "122326"),
    Student("sdf", "男", "004", 22, "125424"),
    Student("sdf", "女", "005", 33, "178512")

]


# 来个管理者的类，控制一些方法管理(增删改查)
class Administrator:

    def __init__(self, name="管理员") -> None:
        super().__init__()
        self.name = name
        self.__admin_login = None
        self.__admin_num = "123456"
        self.__admin_pwd = "000000"

    def admin_login(self):
        # 检测是否已登录
        if self.__admin_login is not None:
            print("请勿重复登录！")
            return
        for j in range(3):
            stu_num = input("请输入管理工号:")
            pwd = input("请输入管理密码:")
            if pwd == self.__admin_pwd and stu_num == self.__admin_num:
                print("登录成功!")
                return
            else:
                if j == 2:
                    print("您已被禁止登录，请联系教务处人员！")
                    return
                print(f"你输入的工号或密码有误，还有{2 - j}次登录机会")

    # 按对象列表添加
    @classmethod
    def sav_list(cls, roles: list, sav_file):
        with open(sav_file, "w", encoding="utf-8") as list_write:
            for role in roles:
                list_write.write(role.__str__())
                list_write.write("\n")

    @classmethod
    def load_all_objs(cls, sav_file):
        ret = []
        with open(sav_file, "r", encoding="utf-8") as read_list:
            str_list = read_list.readlines()
            for i in str_list:
                name = i.split(",")[0]
                gender = i.split(",")[1]
                stu_num = i.split(",")[2]
                score = i.split(",")[3]
                password = i.split(",")[4][:-1]

                ret.append(Student(name, gender, stu_num, score, password))
        return ret

    # 增加对象
    @classmethod
    def append_obj(cls, sav_file, role: Student):
        with open(sav_file, "a", encoding="utf-8")as a_write:
            print(a_write.tell())  # 指针在末尾
            a_write.write(role.__str__())  # 追加对象
            a_write.write("\n")

    # 按学号删除
    @classmethod
    def del_obj(cls, sav_file, role_key: str):
        all_objs = cls.load_all_objs(sav_file)
        for i in all_objs:
            if role_key == i.name:
                all_objs.remove(i)
                break
        cls.sav_list(all_objs, sav_file)

    # 按学号查询，进行修改
    @classmethod
    def update_file(cls, sav_file, role_key: str, new_score, new_password):
        all_objs = cls.load_all_objs(sav_file)
        for i in all_objs:
            if i.name == role_key:
                i.score = new_score
                i.password = new_password
                break
        cls.sav_list(all_objs, sav_file)

    # 从文件按对象查询
    @classmethod
    def query_students(cls, self_stu):
        with open("Students.date", "r", encoding="utf-8") as read_io:

            while True:  # 按原行数读取
                data = read_io.readline(len(str(self_stu)))
                # print(data, len(data))
                # print(self,len(str(self)))
                if data == str(self_stu):
                    return f"找到对象：{self_stu}"
                if not data:
                    return None


admin = Administrator()
admin.admin_login()
admin.sav_list(stus, "Students.date")
admin.load_all_objs("Students.date")
admin.append_obj("Students.date", Student("qws", "男", "007", 23, "196244"))
admin.del_obj("Students.date", "222")
admin.query_students(Student("sfs", "男", "001", 23, "124124"))
admin.update_file("Students.date", "22", 66, "123653")
