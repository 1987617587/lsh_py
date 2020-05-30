# author:lzt
# date: 2019/11/18 16:02
# file_name: ai
import day10.mechine
import day10.animal
class AI(day10.mechine.MiniMechine,
         day10.animal.CHNPerson):
    pass


# 多继承下的功能查询
# AI().run()
# mro():查询多继承中的功能搜查次序
print(AI.mro())
