"""
# author Liu shi hao
# date: 2019/12/4 14:49
# file_name: set_test

"""
set1 = {1, 2, 3, 5, 7, 42, 5, 2, 1, 0}
print(set1)

set2 = set("asfdwefwe35")

set2.add("asd")
set2.add(2)

set2.remove(2)
# set2.remove(2)
# set2.remove(2)

set2.update([1, 2, 3])
# set2.pop()
print(set2)
set2.discard(2)
print(set2)
# set2.clear()
set3 = {1, 2, 3}

print(set2 - set3)  # 差
print(set2 | set3)  # 并
print(set2 & set3)  # 交
set4 = {1}
print(set4.issubset(set3))
print(set4.issuperset(set3))
print(set3.issuperset(set4))


# 集合去重
class Student:

    def __init__(self, name, pid) -> None:
        super().__init__()
        self.name = name
        self.pid = pid

    def __eq__(self, o) -> bool:
        return self.pid == o.pid

    def __hash__(self) -> int:
        return self.pid.__hash__()

    def __str__(self) -> str:
        return f"姓名{self.name}身份证号{self.pid}"


#
# stus = {
#     Student("001", 123),
#     Student("001", 123),
#     Student("002", 122),
#     Student("003", 133)
# }

stus = [
    Student("001", 123),
    Student("002", 322),
    Student("003", 333)

]

for j in stus:
    print(j)

print("*" * 19)

stus_idct = {i.pid: i for i in stus if str(i.pid)[0] == "3"}

# print(stus_idct)
# print(stus_idct.get(stus[0].pid))
# print(stus_idct.get(333))
# print(stus_idct.get(322))
for j in stus_idct.values():
    print(j)













































