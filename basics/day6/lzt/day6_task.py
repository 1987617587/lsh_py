# author:lzt
# date: 2019/11/13 9:55
# file_name: day6_task
# 1、写一个函数，在函数内依次打印出列表每个元素的值。
import random


def task1(arr: list):
    for i in range(len(arr)):
        print(arr[i])


# task1([1, 2, 3, 4])
# task1(["1", "2", "3"])
# task1([True, False])
# task1([1, "123", 1.3])
#
# 2、写一个函数，计算列表所有元素的和(注意返回值)。
def sum_arr(arr: list):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


# print(sum_arr([1, 2, 3, 4, 5]))
#
# 3、写一个函数，计算列表所有奇数索引元素的和(注意返回值)。
def task3(arr: list):
    sum = 0
    for i in range(1, len(arr), 2):
        sum += arr[i]
        pass
    return sum


# print(task3([1, 2, 3, 4, 5]))
#
# 4、写一个函数，计算列表所有偶数索引元素的和(注意返回值)。
def task4(arr: list):
    sum = 0
    for i in range(0, len(arr), 2):
        sum += arr[i]
        pass
    return sum


# print(task4([1, 2, 3, 4, 5]))
#
# 5、写一个函数可以计算两个数的和，想想这个函数有哪些参数，返回值是什么类型。
def task5(num1: int, num2: int):
    return num1 + num2


# print(task5(1, 2))
#
# 6、写一个函数可以计算两个数的商(分母不能为0)，想想这个函数有哪些参数，返回值是什么类型。
def task6(num1: int, num2: int):
    return "错误" if num2 == 0 else num1 / num2


# print(task6(1, 2))
#
# 7、写一个函数将传入的天、小时、分钟、秒的总和转换为秒，比如0天、2小时、5分、7秒，
# 他们代表的总秒数为2*3600+5*60+7=7507秒。想想这个函数有哪些参数，返回值是什么类型。
def task7(days: int, hours: int, minutes: int, seconds: int):
    return days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds


# print(task7(0, 2, 5, 7))
#
# 8、写一个函数交换整型列表中两个指定索引元素的值。想想这个函数有哪些参数，返回值是什么类型。
def task8(arr: list, swap1: int, swap2: int):
    # 做索引的范围的检测
    if swap1 < 0 or swap1 >= len(arr) or swap2 < 0 or swap2 >= len(arr):
        return
    arr[swap1], arr[swap2] = arr[swap2], arr[swap1]
    # return arr


# arr2 = [1, 2, 3, 4, 5, 6, 7]
# task8(arr2, 2, 6)
# print(arr2)
#
# 9、写一个函数计算整型列表中所有能被3整除元素的个数。想想这个函数有哪些参数，返回值是什么类型。
def task9(arr: list):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            count += 1
            pass
        pass
    return count


# print(task9([1, 2, 3, 44, 33, 36]))
#
# 10、写一个函数将整型数字(int)转换为格式化的字符串(str)，现要求如下：
# a.可以指定转换后[字符串的长度];
# b.当数字的长度不足指定的长度，让这个字符串右对齐，指定[左边补的字符(char)];
# 例如，假设现在将指定的数字转换为固定长度为8的字符串，如果长度不足，左边补'0'，
# 那么27这个数字就会转换为字符串"00000027"。
# 根据要求，想想这个函数有哪些参数，返回值是什么类型。
def task10(num: int, str_len: int, pad_char: str):
    # 将数字变为字符串
    num_str = str(num)
    # 按长度左边开始补足位数
    for i in range(str_len - len(num_str)):
        # 怎么在字符串左边补字符
        # +：字符串连字符
        num_str = pad_char + num_str
        pass
    return num_str


# print(task10(123, 10, "#"))

#
# 11.用函数实现找出一个整型列表中最大值和最小值 
def task11(arr: list):
    # return max(arr), min(arr)
    # 检测列表是否为空
    if arr is None or len(arr) == 0:
        return
    # 假设
    # 假设第一个最大又最小
    max_num = arr[0]
    min_num = arr[0]
    # 验证假设是否成立
    for i in range(1, len(arr)):
        # 发现更大或者更小的：更新假设值
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]
    return max_num, min_num


# print(task11([1, 2, 3, 4, 5, 6, 7]))
# print(task11(None))
# print(task11([]))

#
# 12.判断一个数是否是质数(素数)？该如何声明函数？
def task12(num: int):
    # 是否为大于1的自然数
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 1-100之间差值为6的素数对
# for i in range(1, 101):
#     if task12(i) and i + 6 <= 100 and task12(i + 6):
#         print(i, i + 6)
#
# 13. 将指定的秒数转变为几小时几分几秒。
def task13(seconds: int):
    hour = seconds // 3600
    minutes = seconds % 3600 // 60
    second = seconds % 60
    return hour, minutes, second


# ret = task13(10000)
# print(f"小时:{ret[0]} 分钟:{ret[1]} 秒数：{ret[2]}")
#
# 14.使用Random类给一个列表的所有元素赋随机初值（不重复）。
def task14():
    # 为10个位置的列表找到10个各不相同的随机数(1-10)
    # 为每一个位置找不重复的随机数
    # 定义一个列表
    # nums = [0] * 10
    # for i in range(len(nums)):
    #     while 1:
    #         # 为i位置找到和之前位置不同的随机数
    #         random_num = random.randint(1,10)
    #         if random_num not in nums:
    #             nums[i] = random_num
    #             break
    # nums = []
    # while len(nums) != 10:
    #     random_num = random.randint(1, 10)
    #     if random_num not in nums:
    #         nums.append(random_num)
    # return nums

    # 为数字找随机位置:洗牌算法
    # nums = [0] * 10
    # for i in range(1, 11):
    #     while 1:
    #         # i:1-10
    #         # 随机位置
    #         random_index = random.randint(0, len(nums) - 1)
    #         # 找到了一个随机位置
    #         # 判断该位置是否已经有数字了
    #         if nums[random_index] == 0:
    #             nums[random_index] = i
    #             break

    # 使用随机打乱方式获取不重复数据
    nums = list(range(1, 11))
    random.shuffle(nums)
    return nums


# print(task14())


#
# 15.判断一个整型列表是否是对称的。所谓对称就是第一个元素等于最后一个元素，
# 第二个元素等于倒数第二个元素，依次类推，例如【7，3，1，3，7】就是对称的。
def task15(arr: list):
    # 列表不能为None 为空
    if arr is None or len(arr) == 0:
        return False
    for i in range(len(arr) // 2):
        # i,len(arr)-1-i
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
        pass
    return True


# print(task15([1, 2, 3, 4, 2, 1]))

#
# 16.打印一个列表的所有值。
#
# 17.查找一个列表中某个值是否存在，如果存在返回这个值的索引，否则返回-1。
def task17(arr: list, key: int):
    if key not in arr:
        return -1
    return arr.index(key)


# print(task17([1, 2, 3], 2))
#
# 18.将一个列表反转过来，比如【2，3，1，4，7】转换为【7，4，1，3，2】 
def task18(arr: list):
    # arr.reverse()
    return list(reversed(arr))


# arr2 = [1, 2, 3, 4]
# arr2 = task18(arr2)
# print(arr2)
#
# 19.求一个列表的最大值。
#
# 20.求一个列表的最小值。
#
# 21.写一个函数，实现在列表中指定的的位置前插入一个值。
def task21(arr: list, index: int, value: str):
    # 位置的检测
    # index >= len:直接放置在末尾
    # index < 0: 倒着数放置
    arr.insert(index, value)


# arr2 = ["a", "b", "c"]
# task21(arr2, 100, "s")
# print(arr2)
#
# 22.写一个函数，删除列表中指定位置的元素。 
def task22(arr: list, index: int):
    # 对删除位置检测
    if index < -len(arr) or index >= len(arr):
        return
    # 列表的删除
    # 按位置删除
    # 按数据删
    del arr[index]


# arr2 = [1, 2, 3]
# task22(arr2, 3)
# print(arr2)
#
# 23.猜数游戏
# 1.随机出现一个数(范围自定义) 作为答案
# 2.提示用户输入并根据答案和用户输入的大小关系输出大了? 小了?
# 3.5次机会
# 4.可以重复玩
# 5.根据猜对的次数进行评价
# 6.无论对错 请告知答案
def game():
    while 1:
        # 随机一个数字(带数据范围)
        guess = random.randint(1, 100)
        print(guess)
        # 5次机会猜测
        for i in range(5):
            # 请用户输入范围内的数字进行猜测
            user_guess = int(input("请输入1-100之间的数字:"))
            # 做判断和提示
            if user_guess > guess:
                print("大了")
            elif user_guess < guess:
                print("小了")
            else:
                print("猜对了！")
                # 正确的情况下要做评价
                if i == 0:
                    print("运气爆棚！")
                elif i < 3:
                    print("还可以")
                else:
                    print("一般般！")
                # 猜测循环结束了
                break
        # 无论对错都要告知答案
        print(f"答案{guess}")
        # 询问是否继续
        if "y" == input("是否继续?y-不继续 其他-继续"):
            break


game()
