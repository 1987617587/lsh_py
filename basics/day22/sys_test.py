"""
# author Liu shi hao
# date: 2019/12/3 14:46
# file_name: sys_test

"""
import sys

print(sys.path)
# 操作模块sys
# sys模块提供了一系列有关Python运行环境的变量和函数
#
# sys模块常用的功能:
# sys.argv
print(sys.argv)
# 获取当前正在执行的命令行参数的参数列表(list)
# sys.platform
# 获取当前执行环境的平台，如win32表示是Windows 32bit操作系统，linux2 表示是linusys.path  在
# python启动时，sys.path 根据内建规则、PYTHONPATH变量进行初始化。
print(sys.platform)
# sys.builtin_module_names
# 返回一个列表，包含内建模块的名字
#
print(sys.builtin_module_names)
# sys.exit(n)
# 调用sys.exit(n) 可以中途退出程序，当参数非0时，会引发一个SystemExit 异常，从而可以在主程序中捕获该异常。
sys.exit(0)

















































































