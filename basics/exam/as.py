"""
# author Liu shi hao
# date: 2019/11/23 17:36
# file_name: as

"""
# 码表不对哦
allcards = []
for i in range(1, 14):
    for k in range(4):
        if k == 0:
            allcards.append(chr(9824)+str(i))
        elif k == 1:
            allcards.append(chr(9827) + str(i))
        elif k == 2:
            allcards.append(chr(9829) + str(i))
        else:
            allcards.append(chr(9830) + str(i))

print(allcards)