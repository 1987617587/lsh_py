"""
# author Liu shi hao
# date: 2019/12/6 17:06
# file_name: w_r_file_test

"""
# # 非with模式
# write_io = open("write_test1.dat", mode="w", encoding="utf-8")
# # 无法自动换行，需要自行加入换行符
# write_io.write("第一行数据\n")
# write_io.writelines(["第二行数据\n", "第三行数据"])
# write_io.close()
#
# with模式(自动关闭占用资源)
with open("write_test2.date", "w", encoding="utf-8") as io:
    io.write("第一行数据\n")
    io.writelines(["第二行数据\n", "第三行数据"])

# io.writelines("sa")

with open("write_test2.date", "r", encoding="utf-8") as read_io:
    # 规定数据，不要全部读取
    # 用循环的方式 慢慢读取 直到结束
    # while True:  # 按自定义字符数读取
    #     data = read_io.read(10)
    #     if not data:
    #         break
    #     print(data, end="")

    # while True:  # 按原行数读取
    #     data = read_io.readline()
    #     if not data:
    #         break
    #     print(data, end="")

    while True:
        line = read_io.readlines(0)  # 读取之后放到列表中
        if not line:
            break
        print(line)

# print(read_io.readlines(2))
