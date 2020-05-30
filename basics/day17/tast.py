"""
# author Liu shi hao
# date: 2019/11/29 14:35
# file_name: tast

"""
i = 1


# 递归算法，斐波那契数列
def fb(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fb(num - 1) + fb(num - 2)


# print(fb(5))
# # print([fb(x) for x in range(1,34) ])

# dic = dict()
# dic.setdefault("河南", "冷")
# dic.setdefault("浙江", "刚好")
# dic.setdefault("黑龙江", "受不了")
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.get("日本"))
# dic2 = {"河南": "热", "日本": "冷"}
# dic.update(dic2)  # 更新
# print(dic)
# dic["日本"] = "要死"
# print(str(dic))
#
# # 1.
# # 字典.pop(键)
# # 根据键，删除指定的值，并将此值返回
# print(dic.pop("日本"))
# # 2.
# # del 字典[键]
# # 根据键，删除指定的值
# del dic["黑龙江"]
# print(str(dic))
# # 3.
# # 字典.popitem()
# # 随机删除一个
# dic.popitem()
# print(str(dic))
# # 4.
# # 字典.clear()
# # 清空字典里的键值对
# dic.clear()
# print(str(dic))
# li = [i for i in range(5)]
# dic = dict.fromkeys(li, "hah")
# print(str(dic))
arr = ["八", "三", "一"]
li = [i for i in range(3)]
s = "一二三四五六七八九十"
# dic = {"八":8, "三":7, "一":1}

r_arr =[]
for i in range(len(s)):
    for j in range(len(arr)):
        if arr[j] == s[i]:
            r_arr.append(s[i])
            break
print(r_arr)















































