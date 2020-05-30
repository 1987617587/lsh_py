"""
# author Liu shi hao
# date: 2019/11/21 11:46
# file_name: slots_test

"""
class Account:
    __slots__ = ("name","addr")

    def __init__(self,name,addr) -> None:
        super().__init__()
        self.name = name
        self.addr = addr

acc1 = Account("1","asd")
# acc1.money = 1000
def func(self):
    print(self.name)

Account.pri = func
Account.pri(acc1)

str1 = "A123"
x = 16
sum = 0
for i in range(len(str1)-1,-1,-1):
    if str1[i].isdigit():
        sum+= int(str1[i])*x**int(len(str1) - i-1)
    else:
        # j = (ord(str1[i])- 55)
        sum+= (ord(str1[i])- 55) * x ** int(len(str1) - i-1)
    # sum += int(s)
# print(ord("H")**8)
# print((len(str1) - 1)*2)
print(sum)

def switch():
    x = int(input("选择输入数的进制："))
    str1 = input("输入数：")
    sum = 0
    for i in range(len(str1) - 1, -1, -1):
        if str1[i].isdigit():
            sum += int(str1[i]) * x ** int(len(str1) - i - 1)
        else:
            sum += (ord(str1[i]) - 55) * x ** int(len(str1) - i - 1)
    print(sum)
switch()