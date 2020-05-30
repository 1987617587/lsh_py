"""
# author Liu shi hao
# date: 2019/12/7 11:41
# file_name: dict_r_w

"""
class Soldier:
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
        self.pack = {}

    def __str__(self) -> str:
        pack_list = []
        for k,v in self.pack.items():
            pack_list.append(str(k)+"="+str(v))

        return f"{self.name}{','.join(pack_list)}"


def write_dict(sav_file:str,obj:Soldier):
    pass


