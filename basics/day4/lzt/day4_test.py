# author:lzt
# date: 2019/11/11 10:11
# file_name: day4_test
# 1、分别定义int型列表、bool型列表、str型列表
# ints = [1,2,3,4,5]
# bools = [True,False,True]
# strs = ["1"]
#
# 2、定义列表，并赋初值["hello","qikuedu"]，打印出这个列表的长度。
# arr2 = ["hello", "qikuedu"]
# print(len(arr2))
#
# 3、定义一个列表，并赋初值["u","n","i","t","y"]，打印出这个列表最后一个元素的值。
arr3 = ["u", "n", "i", "t", "y"]
# print(arr3[4])
# print(arr3[-1])
# print(arr3[len(arr3) - 1])
#
# 4、定义一个列表，并赋初值[5, 3, 7, 6, 8]，将第4个元素的值修改为原来的2倍，然后分别打印第2个和第4个元素的值。
# arr4 = [5, 3, 7, 6, 8]
# arr4[3] *= 2
# print(arr4[1], arr4[3])
#
# 5、定义一个int型列表，并赋初值[3,2,5,8,4]，打印第3个和第5个元素的值，然后将第3个元素的值与第5个元素的值做交换，
# 再打印这两个元素的值。
# arr5 = [3, 2, 5, 8, 4]
# print(arr5[2], arr5[4])
# arr5[2], arr5[4] = arr5[4], arr5[2]
# print(arr5[2], arr5[4])

#
# 6、定义一个整型列表，使用循环语句(for)给它每个元素赋值，值依次为0,1,2,3,4,... 要求100个元素。
# arr6 = list(range(100))
# print(arr6)
# arr6 = []
# for i in range(100):
#     arr6.append(i)
#     pass
# print(arr6)

#
# 7.一次语文测试后,老师让班长统计每一个学生的成绩并计算全班(全班共3人)的
# 平均成绩、最好成绩、总成绩,然后把所有成绩显示出来.
# 好的解决方法：使用列表.
# ss = []
# while len(ss) != 3:
#     score = float(input("成绩：(0-100)"))
#     if score < 0 or score > 100:
#         print("成绩无效 请重新输入")
#         continue
#     ss.append(score)
#     pass
# print(f"平均成绩:{sum(ss)/len(ss)} 最好成绩:{max(ss)} 总成绩:{sum(ss)}")
# print(ss)
#
# 8.列表里面都是人的名字,以"|"连接:例如:老杨|老苏|老邹…
# ("老杨","老苏","老邹","老虎","老牛","老蒋","老王","老马")
names = ["老杨", "老苏", "老邹", "老虎", "老牛", "老蒋", "老王", "老马"]
# f_names = ""
# for i in range(len((names))):
#     f_names += names[i] + ("|" if i != len(names)-1 else "")
# print(f_names)
# join:以分隔符连接的方式连接列表中的所有元素
# f_names = "|".join(names)
# print(f_names)
# f_names = "*".join(names)
# print(type(f_names))
#
# 9.将一个整数列表的每一个元素进行如下的处理：如果元素是正数则将这个位置的元素的值加1，
# 如果元素是负数则将这个位置的元素的值减1,如果元素是0,则不变。
# arr9 = [-1, 0, 1]
# for i in range(len(arr9)):
#     arr9[i] += 0 if arr9[i] == 0 else (1 if arr9[i] > 0 else -1)
#     pass
# print(arr9)
#
# 10.将一个字符串列表的元素的顺序进行反转。["我","是","好人"]["好人","是","我"]。
msg = ["我", "是", "好人"]
# for i in range(len(msg) - 1, -1, -1):
#     print(msg[i])
#     pass
# print(msg)
# 第一种:列表的函数:reverse
# msg.reverse()
# print(msg)
# 第二种:内置函数 reversed
# msg = list(reversed(msg))
# print(msg)
# 第三种:切片
msg = msg[::-1]
print(msg)

