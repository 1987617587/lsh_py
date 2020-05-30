# author:lzt
# date: 2019/12/7 9:27
# file_name: r_w_objs

# 用字符串的方式读写自定义对象：按格式写出 按格式读回
import os


class Magic:

    def __init__(self, name, hp, atk) -> None:
        super().__init__()
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self) -> str:
        return f"{self.name},{self.hp},{self.atk}"


# m1 = Magic("大傻", 1000, 150)
#
# # 代码要结束了 存储一下角色数据
# # 按字符串的方式存储对象
# # 存档
# with open("sav1.obj","w",encoding="utf-8") as sav:
#     sav.write(m1.__str__())


# 游戏开始
# 游戏读取存档
# role = None
# with open("sav1.obj", "r", encoding="utf-8") as load:
#     obj_strs = load.readline().split("\t")
#     # 拆分字符串 进行对象的重现
#     role = Magic(obj_strs[0], obj_strs[1], obj_strs[2])
#
# # 游戏重新开始
# if role is not None:
#     print(role)

roles = [
    Magic("001是否", 1500, 150),
    Magic("002阿斯顿", 1800, 250),
    Magic("003按时", 1900, 350)
]


# 读写列表
def sav_list(roles: list, sav_file):
    with open(sav_file, "w", encoding="utf-8") as list_write:
        for role in roles:
            list_write.write(role.__str__())
            list_write.write("\n")


# sav_list(roles, "sav_list.csv")

# 读取所有的对象
def load_all_objs(sav_file):
    ret = []
    with open(sav_file, "r", encoding="utf-8") as read_list:
        str_list = read_list.readlines()
        # ["\n"]
        for i in str_list:
            # i是每个对象的字符串表示
            # 拆分成对象的各个属性
            name = i.split(",")[0]
            hp = i.split(",")[1]
            atk = i.split(",")[2][:-1:]
            ret.append(Magic(name, hp, atk))
    return ret

# read_list = load_all_objs("sav_list.objs")
# for i in read_list:
#     print(i)

# read_list = load_all_objs("sav_list.csv")
# for i in read_list:
#     print(i)

# 文件的增加 删除 修改
def append_obj(sav_file: str, role: Magic):
    with open(sav_file, "a", encoding="utf-8") as a_write:
        # a:指针位置在文件末尾
        # a_write.seek(0)
        a_write.write(role.__str__())
        a_write.write("\n")


# print(os.path.getsize("sav_list.csv"))
# append_obj("sav_list.csv", Magic("二傻", 2300, 450))

def del_obj(sav_file: str, role_key: str):
    # 整取
    # 取得所有的对象
    all_objs = load_all_objs(sav_file)

    # 删除文件变成删除列表中内容
    for i in all_objs:
        if role_key == i.name:
            all_objs.remove(i)
            break

    # 列表的内容整存到文件中
    sav_list(all_objs, sav_file)


# del_obj("sav_list.csv", "二傻")
# read_list = load_all_objs("sav_list.csv")
# for i in read_list:
#     print(i)


# 更新文件数据
def update_file(sav_file: str, role_key, new_hp, new_atk):
    # 整取
    all_objs = load_all_objs(sav_file)

    # 文件的修正变为列表内容的修正
    for i in all_objs:
        if i.name == role_key:
            i.hp = new_hp
            i.atk = new_atk
            break

    # 整存
    # 列表的内容整存到文件中
    sav_list(all_objs, sav_file)


# update_file("sav_list.csv", "001是否", 2200, 290)
# read_list = load_all_objs("sav_list.csv")
# for i in read_list:
#     print(i)

