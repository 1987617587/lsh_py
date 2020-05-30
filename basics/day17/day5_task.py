"""
# author Liu shi hao
# date: 2019/11/29 16:42
# file_name: day5_task

"""
import random


def func_1():
    arr = ["八", "三", "一"]
    s = "一二三四五六七八九十"
    r_arr = []
    for i in range(len(s)):
        for j in range(len(arr)):
            if arr[j] == s[i]:
                r_arr.append(s[i])
                break
    return r_arr


# print(func_1())


# 10.为哈希表追加不重复的10个值，且每个值都是1-10之间的随机数，问哪个数字重复的次数最多，重复了多少次？
def func_2(n: int):
    arr1 = [i for i in range(1, n + 1)]
    hash = dict.fromkeys(arr1, 0)
    # while min(hash.values())==0 and sum(hash.values())!=10:
    for i in range(n):
        hash[random.randint(1, 10)] += 1
    print(hash)
    # for i in range(1,11):
    #     hash[i] = random.randint(1,10)
    for j in range(1, 11):
        if hash[j] == max(hash.values()):
            print(f"{j}数字重复的次数最多，重复了{max(hash.values())}次")
    return hash


# print(func_2(10))

# 11.假定书籍的种类有5种，设计何种的数据结构可以达到快速查询某类所有书籍的功能（提示：用Dictionary<K,V>）
# {"科幻":[{"书名":"三体"},{"书名":"未来是什么"}]}
#
dic = {"科幻":[{"书名":"三体"},{"书名":"未来是什么"}],"文学":[{"书名":"西游记"},{"书名":"红楼梦"}]}
print(dic["科幻"])
# 12.citys={"郑州":"晴天","开封":"大雨","北京":"晴天"}
#  转化为：
#  weather={"晴天":["郑州","北京"],"大雨":["开封"]}
#  将  键 变为 值 ，值 变为 键
def func_12():
    fine = []
    rain = []
    citys = {"郑州": "晴天", "开封": "大雨", "北京": "晴天"}
    for key, values in citys.items():
        if values == "晴天":
            fine.append(key)
        if values == "大雨":
            rain.append(key)
    return {"晴天": fine, "大雨": rain}


# print(func_12())


def func10_1():
    dict1 = {"郑州": "晴天", "开封": "大雨", "北京": "晴天"}
    dict2 = {v: [k] for k, v in dict1.items()}
    for k, v in dict1.items():
        li_k = dict2.get(v)
        if k not in li_k:
            li_k.append(k)
    return dict2


# print(func10_1())


def func10_2():
    dict1 = {"郑州": "晴天", "开封": "大雨", "北京": "晴天"}
    dict2 = {v: [i for i in dict1.keys() if dict1.get(i) == v] for k, v in dict1.items()}
    return dict2


print(func10_2())
#
# 思考题：
# 如何用队列实现约瑟夫环
# 约瑟夫环：假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，
# 接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。
#

mydict = {"a": 1, "b": 2, "c": 3}
mydict_new = dict([val, key] for key, val in mydict.items())
print(mydict_new)
