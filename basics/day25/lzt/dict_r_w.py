# author:lzt
# date: 2019/12/7 11:40
# file_name: dict_r_w

class Soldier:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.pack = {}

    def __str__(self) -> str:
        # 将背包的内容变为格式化的字符串
        # a=b,c=d....
        pack_list = []
        for k, v in self.pack.items():
            pack_list.append(str(k) + "=" + str(v))
        return f"{self.name},{','.join(pack_list)}"


def write_dict(sav_file: str, obj: Soldier):
    with open(sav_file, "w", encoding="utf-8") as dict_write:
        dict_write.write(obj.__str__())
        dict_write.write("\n")


# 读取带字典的对象
def read_dict(sav_file):
    with open(sav_file, "r", encoding="utf-8") as read_dict:
        line = read_dict.readline()
        # "001",武器=弓箭,血瓶1=血瓶
        line_split = line.split(",")
        name = line_split[0]
        pack = {}
        for i in range(1, len(line_split)):
            pack[line_split[i].split("=")[0]] = line_split[i].split("=")[1]
        s = Soldier(name)
        s.pack = pack
        return s


# 写出带字典的对象
s1 = Soldier("战士1")
s1.pack["武器"] = "弓箭"
s1.pack["血瓶1"] = "大血瓶"
write_dict("dict_obj.csv", s1)


# 读回带字典的对象
load = read_dict("dict_obj.csv")
print(type(load))
print(load)
