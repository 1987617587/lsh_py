"""
# author Liu shi hao
# date: 2019/12/4 10:35
# file_name: test

"""
t1 = ([1, 2, 3], [2])
t1[0][1] = 1
print(t1)
# t1[0] = [1]
li = [1, 2, 3, 4, 5]
for index, i in enumerate(li, 0):
    # li[1] = 0
    # del li[0]
    del li[0]
    # del li
    print(i, index)
print(li)