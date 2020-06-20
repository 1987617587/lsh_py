# author:lsh
# datetime:2020/4/24 20:07 
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

案例：全球食品添加剂用量分析
1、pandas加载数据
2、按国家分组统计食品添加剂的平均用量
3、柱形图呈现食品添加剂平均用量最多的前十个国家
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1、获取国家和食品添加剂用量
df_obj = pd.read_csv('data/FoodFacts.csv', usecols=['countries_en','additives_n'])
# # print(df_obj)
print('+'*88)
# 丢弃缺失数据：dropna()
df_obj = df_obj.dropna()
print(df_obj)
# 2、按国家分组统计食品添加剂的平均用量
print('+'*88)
df_obj_group = df_obj.groupby('countries_en').mean()
print(df_obj_group)

# 3、柱形图呈现食品添加剂平均用量最多的前十个国家
df_obj_group_sort = df_obj.sort_values(by='additives_n',ascending = False)
top_df_obj = df_obj_group_sort[:10]
print(top_df_obj)
# 开始画图

x = np.arange(10)
y = top_df_obj['additives_n']
width = 0.25 #宽度，偏移量
ax = plt.subplot(1,1,1)
ax.bar(x, y, width, color='r')
#指定x轴标记的位置
ax.set_xticks(x+width)
ax.set_xticklabels(top_df_obj['countries_en'])
plt.show()