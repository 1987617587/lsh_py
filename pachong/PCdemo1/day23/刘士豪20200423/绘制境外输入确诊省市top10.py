# author:lsh
# datetime:2020/4/23 19:48 
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
'''
level 2:
https://news.sina.cn/zt_d/yiqing0121
绘制境外输入确诊省市top10
'''
import json
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd
import numpy as np

data_file = 'yqdata4_23.txt'
with open(data_file, 'r', encoding='utf-8') as file:
    data_str = file.read()
# print(data_str)
# json字符串==》python内置的数据类型
data = json.loads(data_str)
# print(data)
history_ls = data['data']['jwsrTop']
ls = []
for each in history_ls:
    if each['jwsrNum'] == None:
        each['jwsrNum'] = 0
    item = (
    each['jwsrNum'], each['name'], each['ename'])
    ls.append(item)
# print(ls)
df_obj = pd.DataFrame(ls)
# print(df_obj)
# 指定行索引
df_obj.index = np.arange(df_obj.shape[0])
print(df_obj)

# 数据列做类型转换
print(df_obj.dtypes)
df_obj[0] = df_obj[0].astype('int')
# 避免中文显示乱码
mpl.rcParams['font.sans-serif'] = ['SimHei']
print(df_obj.dtypes)


fig, ax = plt.subplots(1)
ax.set_title('境外输入确诊省市TOP10')
ax.set_xlabel('人数')
ax.set_ylabel('城市')
# y轴
y = df_obj[1]
ax.set_yticklabels(y)
ax.set_yticks(range(0,10,1))
# y = np.array(len(df_obj[2]))
x_data = df_obj[0]
y_data = df_obj[1]
# 绘图
bar_height = 0.3
for i in range(len(df_obj[2])-1,-1,-1):
    if i ==0:
        ax.barh(y=i ,width=df_obj[0][i], height=bar_height, color='r', label='累计确诊')
    else:
        ax.barh(y=i ,width=df_obj[0][i], height=bar_height, color='r')


# 显示图例
plt.legend(loc='upper right')
# 保存图片
plt.savefig('境外输入确诊省市top10图.png')

plt.show()


