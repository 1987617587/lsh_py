
# 作业一: 运行一个Python程序需要使用___命令（填空）
# 答：cmd
# 作业二: 编写一个Python程序, 如HelloFriend，当运行时在cmd窗口输入“python
# HelloFriend.py”时，会在控制台输出“张三，你好，欢迎来到Python世界”
print("张三，你好，欢迎来到Python世界")
# 作业三: 编写一个Python程序, 在cmd窗口运行该文件时, 会在控制台输入自己的基本信息.
# 比如: 姓名, 性别, 年龄, 毕业院校, 所学专业...爱好等信息
# name = "刘士豪"
# gender = "男"
# age = 22
# school = "河南科技学院"
# major = "信息工程"
# hobby = "篮球；NBA；王者荣耀"
# print("*********************",
#       "姓名：", name,
#       "性别：", gender,
#       "年龄：", age,
#       "毕业院校：", school,
#       "所学专业：", major,
#       "兴趣爱好：", hobby,
#       "**********************")
name = input("姓名：")
gender = input("性别：")
age = input("年龄：")
school = input("毕业院校：")
major = input("所学专业：")
hobby = input("兴趣爱好：")

# 作业四: 编写一个Python程序, 在cmd窗口运行该文件时, 会在控制台输出如下图的效果
print(''' 
         英雄商城登陆页面
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
            1.注册用户
            2.用户登录
            3.退出系统
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*''')
input("（温馨提示）请输入您的选项：")
