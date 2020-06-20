# author:lsh
# datetime:2020/4/22 20:21 
"""
                                 .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
"""
import json

import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
filename = "yqdata4_23.csv"


arr=np.loadtxt(open(filename, encoding='utf8'),
               dtype=str,
               delimiter=',',)
print(arr)
# 根据审美，把列表反转（使用切片）
arr = arr[::-1]

# 获取日期
pub_datas = arr[:,0]
print(pub_datas)
# 获取现存确诊人数
cn_diagnosisNum = arr[:,1]
print(cn_diagnosisNum)

# 格式转换
cn_diagnosisNum = cn_diagnosisNum.astype(np.int64)
print(cn_diagnosisNum)

# 获取现存疑似人数
cn_susNum = arr[:,2]
print(cn_susNum)
# 格式转换
cn_susNum = cn_susNum.astype(np.int64)
print(cn_susNum)

result = []
result.append([pub_datas, cn_diagnosisNum, cn_susNum])
print(result)



# list==>ndarray
arr = np.array(result)
print(type(arr))
print(arr)

#
fig,ax = plt.subplots(1,figsize=(16,8))
x = np.arange(len(pub_datas))

ax.plot(x,cn_diagnosisNum,color='r',label='现存确诊人数')
ax.plot(x,cn_susNum,color='g',label='现存疑似人数')
new_pub_datas = [pub_datas[i] for i in range(len(pub_datas)) if i%5==0]
new_x = np.arange(len(new_pub_datas))
print(new_x)
# ax.set_xticks(x)
# ax.set_xticklabels(pub_datas,rotation=45)
ax.set_xticks(new_x)
ax.set_xticklabels(new_pub_datas,rotation=45)

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.title('疫情走势图')
# 设置坐标轴的名称
plt.xlabel('时间')
plt.ylabel('人数')
# 显示图例
plt.legend()
# 图上显示具体数据

for x,y in enumerate(cn_diagnosisNum):
    # plt.text()：显示文本
    # 参数1，参数2 设置文本的显示位置
    # 参数3 设置显示的内容
    # 参数ha:控制水平的对齐方式
    # 参数va:控制垂直的对齐方式
    plt.text(x,y+500,'%s'%y,ha='center',va='top')
# # 显示y_data2
for x,y in enumerate(cn_susNum):
    plt.text(x,y+500,'%s'%y,ha='center',va='top')

# 保存图片
plt.savefig('中国疫情走势图.png')
plt.show()
