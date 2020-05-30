"""
# author Liu shi hao
# date: 2019/12/2 14:45
# file_name: str

"""


# str1 = input("请输入:")
# char_counts = [str1.count(ch) for ch in str1]
# print(str1[char_counts.index(max(char_counts))])
def func():
    str2 = input("请输入:")
    j = 0
    if len(str2.split(".")) == 4:
        for i in range(4):
            if str2.split(".")[i].isdigit() and 0 <= int(str2.split(".")[i]) <= 255:
                j += 1
        if j == 4:
            return True
    return False


print(func())
