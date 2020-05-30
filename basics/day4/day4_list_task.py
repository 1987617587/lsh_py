"""
# author Liu shi hao
# date: 2019/11/8 18:57
# file_name: day4_task

"""

# 1、分别定义int型列表、bool型列表、str型列表
# ints = [1,2,3,4,5]
# bools = [True,False,True]
# strs = ["1"]
#

# 2、定义列表，并赋初值["hello","qikuedu"]，打印出这个列表的长度。
#
# list_2 = ["hello","qikuedu"]
# print(len(list_2))

# 3、定义一个列表，并赋初值["u","n","i","t","y"]，打印出这个列表最后一个元素的值。
# #
# list_3 = ["u","n","i","t","y"]
# print(list_3[len(list_3) -1])

# 4、定义一个列表，并赋初值[5, 3, 7, 6, 8]，将第4个元素的值修改为原来的2倍，
# 然后分别打印第2个和第4个元素的值。
# list_4 = [5, 3, 7, 6, 8]
# list_4[3] *= 2
# print(list_4[1],list_4[3])
# 5、定义一个int型列表，并赋初值[3,2,5,8,4]，打印第3个和第5个元素的值，
# 然后将第3个元素的值与第5个元素的值做交换，再打印这两个元素的值。
#
list_5 = [3,2,5,8,4]
print(list_5[2],list_5[4])
list_5[2],list_5[4] = list_5[4],list_5[2]
print(list_5[2],list_5[4])

# 6、定义一个整型列表，使用循环语句(for)给它每个元素赋值，值依次为0,1,2,3,4,... 要求100个元素。
#
# list_6 = []
# for i in range(100):
#     list_6.append(i)
# print(list_6)
# 7.一次语文测试后,老师让班长统计每一个学生的成绩
# 并计算全班(全班共3人)的平均成绩、最好成绩、总成绩,然后把所有成绩显示出来.
# 好的解决方法：使用列表.
#
# list_score = []
# for i in range(3):
#     score = int(input("请输入学生成绩："))
#     list_score.append(score)
# print(f"全班平均成绩{sum(list_score)/3}、最好成绩{max(list_score)}、总成绩{sum(list_score)}")
# 8.列表里面都是人的名字,以“|”连接:例如:老杨|老苏|老邹…
# (“老杨”,“老苏”,“老邹”,“老虎”,“老牛”,“老蒋”,“老王”,“老马”)
#
# list_8 = ["老杨","老苏","老邹","老虎","老牛","老蒋","老王","老马"]
# for i in range(2*len(list_8) - 1):
#     if i %2 !=0:
#         list_8.insert(i,"|")
# print(list_8)
# 9.将一个整数列表的每一个元素进行如下的处理：
# 如果元素是正数则将这个位置的元素的值加1，
# 如果元素是负数则将这个位置的元素的值减1,如果元素是0,则不变。
#
# list_9 = [1,2,3,-1,-2,-3]
# for i in range(len(list_9)):
#     if int(list_9[i]) > 0:
#         list_9[i] = int(list_9[i])+1
#     elif int(list_9[i])<0:
#         list_9[i] = int(list_9[i]) - 1
#     else:
#         pass
# print(list_9)

# 10.将一个字符串列表的元素的顺序进行反转。[“我”,“是”,”好人”][“好人”,”是”,”我”]。
# list_10 = ["我","是","好人"]
#
# list_10[0] ,list_10[1],list_10[2]= list_10[2],list_10[1],list_10[0]
# print(list_10)
# 1、现有列表[1, 2, 3, 4, 5, 6, 7],编写代码使得列表变为[2, 4, 6, 8, 10, 12, 14]，打印列表的所有元素
#
# list2_1 = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(list2_1)):
#     list2_1[i] =int(list2_1[i])*2
#     print(list2_1[i])
# 2、现有列表[1, 2, 3, 4]和列表[4, 3, 2, 1]，编写代码使得两个列表对应索引的
# 元素相加，并赋值给一个新的列表，打印新列表的所有元素。
#
# list2_23 = []
# list2_21 = [1, 2, 3, 4]
# list2_22 = [4, 3, 2, 1]
# for i in range(4):
#     list2_23.append(int(list2_21[i])+int(list2_22[i]))
# print(list2_23)
# 3、输入5个数，求其中最小值，打印出来。
#
# list2_3 = []
# for i in range(5):
#     in_num = int(input("请输入数："))
#     list2_3.append(in_num)
# print(min(list2_3))
# 4、让用户输入长方形的长和宽，然后显示出此长方形的周长
#
#
# length = int(input("请输入长方形的长："))
# wide = int(input("请输入长方形的宽："))
# print((length + wide)*2)


# 5、编写一个程序，判断用户输入的a、b、c值，能否构成一个三角形？
#

# list2_5 = []
# for i in range(3):
#     list2_5.append(int(input("请输入三角形的边:")))
# if list2_5[0] + list2_5[1]>list2_5[2] and list2_5[0] >0 and list2_5[1]>0 and list2_5[2]>0:
#     print("能构成一个三角形")
# else:
#     print("不能构成一个三角形")


# 6、打印输出1000以内可被3整数除的正整数，每行显示10个数
#
# s = 0
# line_num  = 0
# while s<1001:
#     s += 1
#     if s %3 ==0:
#         line_num += 1
#         print(s,end="\t")
#         if line_num %10 ==0:
#             print()

# 7、循环接收N个整数，直到用户输入0结束。打印出这些数里的最大数和最小数。
#
# list2_7 = []
# while 0 not in list2_7:
#     list2_7.append(int(input("请输入整数：")))
#
# print(f"最大数为{max(list2_7)}最小数为{min(list2_7)}")
# 8、接收学生分数判断区间，学生分数必须在0-100之间，
# 如果不满足，则提醒用户输入，直到输入一个正确的分数为止。
#
# list2_8 = []
# while True:
#     list2_8.append(int(input("请输入整数：")))
#     if 0 > min(list2_8) or  100> min(list2_8):
#         break
# print(list2_8)
# 9、接收10个整数，计算其中正整数的总和，如果其中用户输入999则循环结束。
#
# list2_9 = []
# for i in range(10):
#     list2_9.append(int(input("请输入整数：")))
#     if 999 in list2_9:
#         break
# print(sum(list2_9)-999)
# 10、求1-100之间个位数字不是2，3，4，7，并且不能被3整除的整数之和
#
# list10 = [2,3,4,7]
# list2_10 = []
# for i in range(1,101):
#     if i % 10 not in list10 and i%3!= 0:
#         list2_10.append(i)
# print(sum(list2_10))
# 11、输出1900 到今年之间所有的闰年，并且统计个数（能被 4 整除 但是不能被100整除 或者能被四百整除）
#
# list2_11 = []
# for i in range(1900,2019):
#     if i % 4 ==0 and i%100!= 0 or i%400 ==0:
#         list2_11.append(i)
# print(f"1900 到今年之间所有闰年为{len(list2_11)}个。")
# 12、将一个列表逆序输出
# list2_12 = [1,2,4,5,7,9]
# # list12 = []
# # for i in range(len(list2_12)-1,-1,-1):
# #     list12.append(list2_12[i])
# # print(list12)
# list2_12.reverse()  # 反序是一个动作，没有返回值，Nona
# print(list2_12)  # 不会使用反序
# 13、输入列表,元素不会重复（自定义即可），最大的与第一个元素交换，
# 最小的与最后一个元素交换，输出列表。
# list2_13 = [3,2,4,9,7,1]
# a = max(list2_13)
# b = min(list2_13)
# for i in range(len(list2_13)):
#     if list2_13[i] == a:
#         list2_13[i],list2_13[0]= list2_13[0],list2_13[i]
#         if list2_13[i] == b:
#             list2_13[i] ,list2_13[len(list2_13)-1]= list2_13[len(list2_13)-1],list2_13[i]
#             break
# print(list2_13)

# 14、青年歌手参加歌曲大奖赛，有10个评委进行打分，试编程求这位选手的平均得分
# （去掉一个最高分和一个最低分）。
# list_mark=[]
# for i in range(1,11):
#     list_mark.append(int(input(f"请第{i}个评委打分：")))
# print((sum(list_mark)-min(list_mark)-max(list_mark))/8)
# 15、定义一个列表，并赋初值[5, 3, 7, 6, 8]，将第4个元素的值修改为原来的3倍，
# 然后分别打印下标是奇数的元素。
#
# list2_15 = [5, 3, 7, 6, 8]
# list2_15[3] *= 3
# for i in range(len(list2_15)):
#     if i %2 ==1:
#         print(list2_15[i])
# 16、用户输入一个最大值n表示列表元素数,创建列表存数，数字是所有小于n的偶数
# import random
# list2_16 = []
# list2_even = []
# n = int(input("输入一个最大值n:"))
# for i in range(n):
#     if i % 2 == 0:
#         list2_even.append(i)
#
# list2_16 = list2_even
# for j in range(n-len(list2_even)):
#     list2_16.append(random.choice(list2_even))
# print(list2_16)
# random.shuffle(list2_16)   # s随机打乱列表内的元素
# print(list2_16)
#
# # 17、列表[1, 2, 4, 4, 5, 7, 8]，编写代码删掉列表中的所有4
#
# list2_17 = [1, 2, 4, 4, 5, 7, 8]
# while 4 in list2_17:
#     list2_17.remove(4)
# print(list2_17)
# 选做题：
# 1、将一个英文句子中的前后单词逆置（单词之间用空格隔开）。
# 如：how old are you 逆置后为：you are old how
# list_words = []
# list_1 = []
# while 1:
#     str_1 = input("请输入单词(用空格结束单词):")
#     if " " in str_1:
#         list_1.append(str_1)
#     elif "." in str_1:   # 用户输入“.”结束
#         break
# # for i in range(len(list_1)-1,-1,-1):
# #     print(list_1[i])
# list_1.reverse()
# print(list_1)


# list_1= []
# list_choose1 = ["how ","old", "are ","you "]
# print(list_choose1)
# for i in range(len(list_choose1)-1,-1,-1):
#     list_1.append(list_choose1[i])
#
# print(list_1)
# 2、公交报站系统，每经过一站，报出该站名称，若乘客在该站下车，
# 在出站口提示“一共乘坐x站”。用while循环实现以上程序
#
list_stand = ["人民路","幸福路","长寿街","富民街"]
list_choose1 = []
num_stands = 0
while "y" not in list_choose1 :
    num_stands += 1
    if num_stands >=len(list_stand):
        print(f"终点站{list_stand[num_stands - 1]}到了，一共乘坐{len(list_stand) }站,请下车")
        break
    list_choose1.append(input(f"第{num_stands}站{list_stand[num_stands - 1]}到了，是否下车："))
else:
    print(f"一共乘坐{num_stands }站")
# 3、有一电文，已按下列规律译成译码：
#               A→Z  a→z
#               B→Y  b→y
#               C→X  c→x
#               …    …
# 即第一个字母变成第26个字母，第i个字母变成第(26-i+1)个字母。
# 非字母字符不变。编写一个程序将密码译成原文，并输出密码和原文。
#
#
list_a_z = [chr(i) for i in range(97,123)]
# list_z_a = [chr(i) for i in range(122,96,-1)]
list_A_Z = [chr(i) for i in range(65,91)]
# list_Z_A = [chr(i) for i in range(90,64,-1)]

print(list_a_z)
print(list_A_Z )
# print(list_Z_A )
# print(list_z_a )
list_text = list(input("请输入原文："))
print(f"原文：{list_text}")
for i in range(len(list_text)):
    if list_text[i] in list_a_z :
            list_text[i] = list_a_z[25-list_a_z.index(list_text[i])]
    if list_text[i] in list_A_Z:
            list_text[i] = list_A_Z[25-list_A_Z.index(list_text[i])]

print(f"译文：{list_text}")

# 4、计算圆周率：PI＝4/1－4/3+4/5-4/7.......
# list1_choose4 = []
# list2_choose4 = []
# for i in range(int(input("请输入："))):
#     if i %2 ==0:
#         list2_choose4.append(4/(2*i+1))
#     else:
#         list1_choose4.append(4/(2*i+1))
# print(sum(list2_choose4)-sum(list1_choose4))
# 5、定义一个20*3的二维列表，用来存储某班级20位学员的3门课的成绩；
#  这3门课按存储顺序依次为：Python，Java，C#.
#  (1)循环给二维列表的每一个元素赋0~100之间的随机整数。
#  (2)按照列表的方式输出这些学员的每门课程的成绩。
#  (3)要求编写程序求每个学员的总分，将其保留在另外一个一维列表中。
#  (4)要求编写程序求所有学员的某门课程的平均分。
#
import random

#
# list_score = []
# list_sum = []
# list_Python = [random.randint(0,100) for i in range(20)]
# list_Java = [random.randint(0,100) for j in range(20)]
# list_C = [random.randint(0,100) for k in range(20)]
# list_score.append(list_Python )
# list_score.append(list_Java )
# list_score.append(list_C )
# print(list_score)
# for i in range(20):
#     list_sum.append(list_Python[i]+list_Java[i]+list_C[i])
#     print(f"第{i+1}个学员的总分为{list_Python[i]+list_Java[i]+list_C[i]}")
# print(f"Python课程的平均分为{sum(list_Python)/20},Java课程的平均分为{sum(list_Java)/20},C#课程的平均分为{sum(list_C)/20},")
# print(f"每个学员的三门成绩总分依次为{list_sum}")
#
#







































































