# author:lzt
# date: 2019/11/15 11:16
# file_name: self_test
class Person:

    # 初始化方法的self代表了要出生的对象
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name

    # 为了区分局部变量和成员变量同名的情况:
    # 对象的变量:self.
    # 局部变量无需追加self.
    def change_name(self,name):
        self.name = name

    def __del__(self):
        print(f"{self.name}即将死去 是保存到临时文件还是存到数据库 还是释放资源！")



p1 = Person("001")
p2 = Person("002")
# 成员方法如何区分当前调用的对象是谁?
p2.change_name("003")
p1.change_name("000")
print(f"p1.name={p1.name} p2.name={p2.name}")

# 对象的内存消亡时机：
# 1.程序退出时 内存要清理

# 2.程序持续运行中 a.对象成为孤岛 b.垃圾回收器开始回收
p1 = None
p2 = None
# import gc
# # 强制垃圾回收！！！
# gc.collect()
input()
