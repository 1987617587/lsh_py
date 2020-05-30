# author:lzt
# date: 2019/11/18 15:06
# file_name: xuzhu_test
class ShaoLin:

    def __init__(self, sl_years, xy_years, lj_years) -> None:
        super().__init__(xy_years, lj_years)
        self.name = "少林寺"
        self.sl_years = sl_years

    def yijinjing(self):
        print("易筋经")


class XiaoYao:
    def __init__(self, xy_years, lj_years) -> None:
        super().__init__(lj_years)
        self.name = "逍遥"
        self.xy_years = xy_years

    def beiming(self):
        print("北冥神功")


class LingJiu:
    def __init__(self, lj_years) -> None:
        super().__init__()
        self.name = "灵鹫宫"
        self.lj_years = lj_years

    def shengsifu(self):
        print("生死符")


class XuZhu(ShaoLin, XiaoYao, LingJiu):
    pass


xz1 = XuZhu(16, 60, 110)
xz1.yijinjing()
xz1.beiming()
xz1.shengsifu()
print(xz1.lj_years)
