"""
# author Liu shi hao
# date: 2019/12/3 18:41
# file_name: day22_list_task

"""


# 作业一
# 自定义一个学生类，属性有 姓名 年龄，如果用户在给学生年龄赋值时，
# 年龄小于0抛出一个AgeLT0Exception，大于150  抛出一个AgeGT150Exception
class AgeLT0Exception(Exception):

    def __init__(self, name, set_age) -> None:
        super().__init__()
        self.name = name
        self.set_age = set_age

    def __str__(self) -> str:
        return f"异常发生的学生姓名是{self.name}，" \
            f"情况为赋值年龄{self.set_age}小于0"


class AgeGT150Exception(Exception):

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"异常发生的学生姓名是{self.name}，" \
            f"情况为赋值年龄{self.age}大于150"


class Student:
    def __init__(self, name, age) -> None:
        super().__init__()
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            self.__age = 0
            raise AgeLT0Exception(self.name, value)
        if value > 150:
            self.__age = 0
            raise AgeGT150Exception(self.name, value)
        self.__age = value


if __name__ == '__main__':
    try:
        s = Student("sa", 199)
        # s.age = 199
    except AgeGT150Exception as e:
        print(e)
    except AgeLT0Exception as e:
        print(e)


# 1.	向列表[1, 2, 3, 4, 5]插入20，30，40
def func_1():
    list1 = [1, 2, 3, 4, 5]
    list1.insert(1, 20)
    list1.insert(2, 30)
    list1.insert(3, 40)
    return list1


# print(func_1())
# 2.	从列表[1, 2, 3, 4, 5]删除4，5
def func_2():
    arr = [1, 2, 3, 4, 5]
    arr.remove(4)
    arr.remove(5)
    return arr


# print(func_2())

# 3.	找到列表[5,3,5,7,4,6,8,3,6]中第一个最小元素的下标
def func_3(arr: list):
    return arr.index(min(arr))


# print(func_3([5, 3, 5, 7, 4, 6, 8, 3, 6]))

# 4.	创建列表,元素为1-1000以内的偶数

# print([i for i in range(1, 1001) if i % 2 == 0])

# 5.	将'My name is Jack, Your name is Rose'转换成列表
# (1)	并截取里面的前10个字符
# (2)	并截取里面的后4个字符
arr5 = list('My name is Jack, Your name is Rose')


def func_5_1(arr: list):
    return arr[0:10]


# print(func_5_1(arr5))


def func_5_2(arr: list):
    r_arr = arr[-4::]
    return r_arr


# print(func_5_2(arr5))

# 6.	[1,2,4,5,6,7,3,2,6,3,2],打印出列表中每个数字出现的次数
def func_6(arr: list):
    for i in range(10):
        if i in arr:
            print(f"{i}出现{arr.count(i)}次数")


# func_6([1, 2, 4, 5, 6, 7, 3, 2, 6, 3, 2])

# 7.	从['P','Y','T','H','O','N']挑出一个字母和['G','O','O','D']挑出一个字母有多少种组合,将各组合方式打印出来
def func_7(arr1: list, arr2: list):
    arr = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if [arr1[i], arr2[j]] not in arr:
                arr.append([arr1[i], arr2[j]])
    print(len(arr))
    return arr


# print(func_7(['P', 'Y', 'T', 'H', 'O', 'N'], ['G', 'O', 'O', 'D']))

# 8.	列表[1,2,3,4,5],需要用户输入数字，然后删除列表中输入数字对应下标的元素
def func_8(arr: list):
    try:
        n = input("输入数字：")
        del arr[int(n)]
        return arr
    except:
        print("格式有误，或超出索引,操作失败！")
        return arr


# print(func_8([1, 2, 3, 4, 5]))

# 9.	列表[100,33,55,2,56,66,22],依次打印每一个元素，然后从列表中删除，直到列表没有元素
def func_9(arr: list):
    n = len(arr)
    for i in range(n):
        print(arr[0])
        del arr[0]
        if len(arr) == 0:
            return arr


# print(func_9([100, 33, 55, 2, 56, 66, 22]))

# 10.	将1-100以内的平方数放入列表，打印列表
def func_10():
    return [i ** 2 for i in range(1, 12) if i ** 2 < 101]


# print(func_10())


# 11.	创建列表，循环向列表依次中放入1个数字，达到100个后，依次删除所有的元素，删除完后，
# 继续循环向列表依次中放入1个数字，达到100个后，依次删除所有的元素.......依次类推
def func_11():
    while True:
        a = []
        for i in range(100):
            s = input("1个数字:")
            a.append(s)
        for j in range(100):
            del a[0]


# func_11()

# 12.	l1 = [2,4,6,8,10]和 l2 = [5,4,2,6,7,8],编写程序求出l2和l1共有的元素
def func_12(arr1: list, arr2: list):
    arr = []
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            arr.append(arr1[i])
    return arr


# print(func_12([2, 4, 6, 8, 10], [5, 4, 2, 6, 7, 8]))

# 13.	[‘book’,’shoe’,’bullet’,’brush’,’car’]将列表中所有包含字母’b’的单词放入新列表中，打印出来
def func_13(arr: list):
    li = []
    for i in range(len(arr)):
        if "b" in arr[i]:
            li.append(arr[i])
    return li


# print(func_13(["book", "shoe", "bullet", "brush", "car"]))

# 14.	用户输入字符串，将字符串转换成列表，如果字符超过5个，只打印用户输入的前5个字符
def func_14(s: str):
    s = list(s)
    if len(s) > 5:
        return s[0:5]
    return s


# print(func_14("asd"))

# 15.	列表【1，2，3，4，5】，循环删除列表的第一个元素，并将它放到列表的后面，打印每一次删除后列表的状态
def func_15(arr: list):
    while True:
        arr.append(arr[0])
        del arr[0]
        print(arr)


# print(func_15([1, 2, 3, 4, 5]))

# 16.	['P','Y','T','H','O','N',’I’,’S’,’V’,’E’,’R’,’Y’,’G’,’O’,’O’,’D’]将列表中的所有’Y’替换成’*’
def func_16(arr: list):
    s = "".join(arr)
    return s.replace('Y', "*")


# print(func_16(['P', 'Y', 'T', 'H', 'O', 'N', 'I', 'S', 'V', 'E', 'R', 'Y', 'G', 'O', 'O', 'D']))

# 17.	['P','Y','T','H','O','N',’I’,’S’,’V’,’E’,’R’,’Y’,’G’,’O’,’O’,’D’]删除列表中出现次数最多的字母
def func_17(arr: list):
    char_counts = [arr.count(ch) for ch in arr]
    num = arr[char_counts.index(max(char_counts))]
    while num in arr:
        arr.remove(num)
    return arr


print(func_17(['P', 'Y', 'T', 'H', 'O', 'N', 'I', 'S', 'V', 'E', 'R', 'Y', 'G', 'O', 'O', 'D']))


# 18.	[3,6,5,7,3,5,7,8,9,9] 删除列表中所有最大的元素
def func_18(arr: list):
    num_max = max(arr)
    while num_max in arr:
        arr.remove(num_max)
    return arr


# print(func_18([3, 6, 5, 7, 3, 5, 7, 8, 9, 9]))

# 19.	[4,5,7,3,6,7,8,6]编写程序查找程序中第二大的元素，打印出
def func_19(arr: list):
    num_max = max(arr)
    while num_max in arr:
        arr.remove(num_max)
    print(max(arr))


# func_19([4, 5, 7, 3, 6, 7, 8, 6])

# 20.	[‘book’,’shoe’,’bullet’,’brush’,’car’]将列表中的每个元素重复5遍放入新的列表
def func_20(arr: list):
    li = []
    for i in range(len(arr)):
        li.append(arr[i] * 5)
    return li


# print(func_20(['book', 'shoe', 'bullet', 'brush', 'car']))

# 21.	[1,2,3,4,5,6,7,8,9]交换列表第一个和最后一个元素的位置

def func_21(arr: list):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


# print(func_21([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 22.	对[1,2,3,4,5,6,7,8,9]每一个元素和5求异或
def func_22(arr: list):
    li = []
    for i in range(len(arr)):
        li.append(arr[i] ^ 5)
    return li


# print(func_22([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 23.	[True,False,True,True,False]，对列表中每个元素取反
def func_23(arr: list):
    for i in range(len(arr)):
        arr[i] = not arr[i]
    return arr


# print(func_23([True, False, True, True, False]))

# 24.	使用循环创建列表，如下[[1], [1,2] ,[1,2,3,],[1,2,3,4],[1,2,3,4,5] ]
def func_24(n: int):
    arr = []
    for i in range(1, n + 1):
        arr.append([j + 1 for j in range(i)])
    return arr


# print(func_24(5))

# 25.	使用循环创建列表，如下[[1,2,3,4,5] ,[1,2,3,4],[1,2,3],[1,2],[1]]
def func_25(n):
    arr = []
    for i in range(n, 0, -1):
        arr.append([j + 1 for j in range(i)])
    return arr


print(func_25(5))
print([list(range(1, i + 1)) for i in range(1, 6)])
print([list(range(1, i + 1)) for i in range(5, 0, -1)])
