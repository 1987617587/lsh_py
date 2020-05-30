print("hello,word!")
print("你好，世界！")
sum = 0
for i in range(101):
    sum = sum + i
print(sum)
def fun_1(s):
    for j in range(s):
        if j % 2 == 0:
            print("*" * (2*j - 1))
        else:
            print(" " * (2 * s - (2*j - 1)) + "*" * (2*j - 1))
    pass
fun_1(7)
