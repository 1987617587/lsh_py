"""
# author Liu shi hao
# date: 2019/11/14 14:23
# file_name: global

"""
date =100
def fun_1():
    date = 111
    print(date)
    print(globals()["date"])
    globals ()["date"] = 222
    print(globals()["date"])

fun_1()






