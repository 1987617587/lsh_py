"""
# author Liu shi hao
# date: 2019/11/18 16:13
# file_name: ai

"""
import day10.animal
import day10.mechine


class AI(day10.mechine.MineMechine, day10.animal.CHNPerson):
    pass


print(AI.mro())
