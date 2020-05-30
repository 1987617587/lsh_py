"""
# author Liu shi hao
# date: 2019/12/7 9:39
# file_name: r_w_objs

"""
import os


class Magic:
    def __init__(self, name, hp, atk) -> None:
        super().__init__()
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self) -> str:
        return f"{self.name},{self.hp},{self.atk}"


# m1 = Magic("吕布", "1000", "200")

# with open("sav1.obj", "w",encoding="utf-8") as sav:
#     sav.write(m1.__str__())

# role = None
# with open("sav1.obj", "r", encoding="utf-8") as load:
#     obj_strs = load.readline().split("\t")
#     role = Magic(obj_strs[0], obj_strs[1], obj_strs[2])
#
# if role is not None:
#     print(role.name)


#
def sav_list(roles: list, sav_file):
    with open(sav_file, "w", encoding="utf-8") as list_write:
        for role in roles:
            list_write.write(role.__str__())
            list_write.write("\n")


roles = [Magic("吕布", "1000", "200"),
         Magic("吕布", "1000", "200"),
         Magic("吕布", "1000", "200"),
         Magic("吕布", "1000", "200")]


# sav_list(roles,"roles.csv")
def load_all_objs(sav_file):
    ret = []
    with open(sav_file, "r", encoding="utf-8") as read_list:
        str_list = read_list.readlines()
        for i in str_list:
            name = i.split(",")[0]
            hp = i.split(",")[1]
            atk = i.split(",")[2][:-1]

            ret.append(Magic(name, hp, atk))
    return ret


# rend_list = load_all_objs(r"E:\python1911A\day25_2\roles.csv")


# for i in rend_list:
#     print(i)


# 改逗号，转.csv文件 用wps打开


# 增加对象
def append_obj(sav_file, role: Magic):
    with open(sav_file, "a", encoding="utf-8")as a_write:
        print(a_write.tell())  # 指针在末尾
        a_write.write(role.__str__())  # 追加对象
        a_write.write("\n")


# append_obj("roles.csv", Magic("貂蝉", "212", "234"))
# print(os.path.getsize("roles.csv"))


# 删除对象
def del_obj(sav_file, role_key: str):
    all_objs = load_all_objs(sav_file)
    for i in all_objs:
        if role_key == i.name:
            all_objs.remove(i)
            break
    sav_list(all_objs, sav_file)


# del_obj("roles.csv", "貂蝉")


# 修改对象
def update_file(sav_file, role_key: str, new_hp, new_atk):
    all_objs = load_all_objs(sav_file)
    for i in all_objs:
        if i.name == role_key:
            i.hp = new_hp
            i.atk = new_atk
            break
    sav_list(all_objs, sav_file)


# update_file("roles.csv", "貂蝉", "222", "121")
# read_list = load_all_objs("roles.csv")
# for i in read_list:
#     print(i)


