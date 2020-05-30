"""
# author Liu shi hao
# date: 2019/11/22 20:43
# file_name: base4

"""


# 13、
# 写一个Cube类:
# 字段：x,y,z坐标，缩放比例 scale_x，scale_y，scale_z
# 字段为公共的访问级别
# 要求：
# 13-1.创建不同位置、不同缩放比例的Cube，创建5个并放入列表中。
# 13-2.打印出x,y,z缩放比例都小于1的Cube的位置及缩放信息。
# 请测试上面的要求.

class Cube:

    def __init__(self, x, y, z, scale_x, scale_y, scale_z) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.scale_z = scale_z

    def __str__(self) -> str:
        return f"x,y,z坐标，缩放比例分别为 {self.scale_x}\t{self.scale_y}\t {self.scale_z}\t"


cube_list = [
    Cube(1, 2, 3, 1.3, 3.4, 0.1),
    Cube(1, 2, 32, 0.3, 0.4, 0.1),
    Cube(10, 2, 31, 0.3, 0.2, 0.1),
    Cube(12, 2, 3, 4.3, 3.4, 0.1),
    Cube(14, 22, 3, 1.7, 3.4, 0.1)
]


def get_ratio():
    for i in range(len(cube_list)):
        if cube_list[i].__class__ == Cube and cube_list[i].scale_x < 1 \
                and cube_list[i].scale_y < 1 and cube_list[i].scale_z < 1:
            print(cube_list[i])


get_ratio()
