#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import json
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd
import numpy as np

data_file = './data/yqdata4_23.txt'
with open(data_file, 'r', encoding='utf-8') as file:
    data_str = file.read()
# print(data_str)
# json字符串==》python内置的数据类型
data = json.loads(data_str)
# print(data)
history_ls = data['data']['historylist']
ls = []
for each in history_ls:
    if each['cn_susNum'] == None:
        each['cn_susNum'] = 0
    item = (
    each['date'], each['cn_conNum'], each['cn_deathNum'], each['cn_cureNum'], each['cn_susNum'], each['cn_econNum'])
    ls.append(item)
# print(ls)
df_obj = pd.DataFrame(ls)
# print(df_obj)

# 按照日期做升序排序
df_obj = df_obj.sort_values(by=0)
# 指定行索引
df_obj.index = np.arange(df_obj.shape[0])
# print(df_obj)
# 数据列做类型转换
print(df_obj.dtypes)
df_obj[1] = df_obj[1].astype('int')
df_obj[2] = df_obj[2].astype('int')
df_obj[3] = df_obj[3].astype('int')
df_obj[4] = df_obj[4].astype('int')
df_obj[5] = df_obj[5].astype('int')
# print(df_obj.dtypes)

# 避免中文显示乱码
mpl.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(1)
ax.set_title('全国疫情趋势图')
ax.set_xlabel('日期')
ax.set_ylabel('人数')
# 处理日期
ls_date = df_obj[0].tolist()


def func(n):
    return ls_date.index(n) % 5 == 0


f = filter(func, ls_date)
ls_date = list(f)
print(ls_date)
# 水平轴，设置显示范围
ax.set_xlim([0, df_obj.shape[0]])
# 设置刻度显示位置
ax.set_xticks(range(0, df_obj[0].shape[0], 5))
# 显示刻度标签
ax.set_xticklabels(ls_date, rotation=45)
# 绘图
colors = ['#E82250', '#18122B', '#2E8714', '#8F1AC9', '#0ED3BF']
labels = ['累计确诊', '累计死亡人数', '累计治愈', '现存疑似', '现存确诊']
for i in range(5):
    ax.plot(df_obj[i + 1], linestyle='solid', marker='.', color=colors[i], label=labels[i])
# 显示图例
plt.legend(loc='upper left')
# 网格线
ax.margins(x=0, y=0.25)
ax.grid(True, axis='y', linestyle='-.')
# 设置鼠标移动的交互事件
# 显示文本的标签
# 参数1，2：文本显示的横坐标和纵坐标
# 参数3：显示内容
# 参数fontsize:设置字号大小
# 参数color:指定颜色
# 参数bbox：设置背景框
text0 = plt.text(0, 0, 'xxx', fontsize=10, color='k', bbox=dict(facecolor='w', alpha=0.3))
line_x = plt.axhline(y=-40, c='#999999', ls='--', lw=1)
line_y = plt.axvline(x=-40, c='#999999', ls='--', lw=1)


def on_mouse(event):
    # print('on mouse...')
    try:
        x = int(np.round(event.xdata))
        y = int(np.round(event.ydata))
        # print('x:',x,' y:',y)
        line_x.set_ydata(y)
        line_y.set_xdata(x)
        data = df_obj.iloc[x, :]
        data = '日期：' + data[0] + '\n' + \
        '累计确诊：' + str(data[1]) + '\n' + \
        '累计死亡：' + str(data[2]) + '\n' + \
        '累计治愈：' + str(data[3]) + '\n' + \
        '现存疑似：' + str(data[4]) + '\n' +\
        '现存确诊：' + str(data[5]) + '\n'
        #print(data)
        text0.set_text(data)
        text0.set_position((x,y))
    except Exception as e:
        text0.set_position((-40,0))
        line_x.set_ydata(-40)
        line_y.set_xdata(-40)
        print(e)
    # 把绘图动作实时反映在图像上
    fig.canvas.draw_idle()


fig.canvas.mpl_connect('motion_notify_event', on_mouse)
# fig.canvas.mpl_connect('figure_enter_event',on_mouse)

plt.show()
