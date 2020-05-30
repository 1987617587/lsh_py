# 13、
# 写一个Cube类:
# 字段：x,y,z坐标，缩放比例 scale_x,scale_y,scale_z
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
        return f"{self.x} {self.y} {self.z} {self.scale_x} {self.scale_y} {self.scale_z}"


cubes = [
    Cube(0, 0, 0, 1, 1, 1),
    Cube(1, 1, 1, 0.8, 0.9, 0.6),
    Cube(2, 2, 2, 1, 1, 1),
    Cube(3, 3, 3, 1, 1, 1),
    Cube(4, 4, 4, 1, 1, 1),
]

for i in range(len(cubes)):
    if cubes[i].scale_x < 1 and cubes[i].scale_y < 1 and cubes[i].scale_z < 1:
        print(cubes[i])
