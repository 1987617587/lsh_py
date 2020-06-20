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
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

filename = "epidemic_information.csv"

arr = np.loadtxt(open(filename, encoding='utf8'),
                 dtype=str,
                 delimiter=',', )
print(arr)
# 根据审美，把列表反转（使用切片）
arr = arr[::-1]

# 获取日期
pub_datas = arr[:, 0]
print(pub_datas)
# 获取现存确诊人数
cn_diagnosisNum = arr[:, 1]
print(cn_diagnosisNum)

# 格式转换
cn_diagnosisNum = cn_diagnosisNum.astype(np.int64)
print(cn_diagnosisNum)

# 获取现存疑似人数
cn_susNum = arr[:, 2]
print(cn_susNum)
# 格式转换
cn_susNum = cn_susNum.astype(np.int64)
print(cn_susNum)

result = []
result.append([pub_datas, cn_diagnosisNum, cn_susNum])

# list==>ndarray
arr = np.array(result)
print(type(arr))
print(arr)

#
fig, ax = plt.subplots(1, figsize=(16, 8))
x = np.arange(len(pub_datas))

ax.plot(x, cn_diagnosisNum, color='r', label='现存确诊人数')
ax.plot(x, cn_susNum, color='g', label='现存疑似人数')
ax.set_xticks(x)
ax.set_xticklabels(pub_datas, rotation=45)

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.title('疫情走势图')
# 设置坐标轴的名称
plt.xlabel('时间')
plt.ylabel('人数')
# 显示图例
plt.legend()
# 图上显示具体数据
#
# for x,y in enumerate(cn_diagnosisNum):
#     # plt.text()：显示文本
#     # 参数1，参数2 设置文本的显示位置
#     # 参数3 设置显示的内容
#     # 参数ha:控制水平的对齐方式
#     # 参数va:控制垂直的对齐方式
#     plt.text(x,y+500,'%s'%y,ha='center',va='top')
# # # 显示y_data2
# for x,y in enumerate(cn_susNum):
#     plt.text(x,y+500,'%s'%y,ha='center',va='top')


# 交互事件
# https://blog.csdn.net/Kwoky/article/details/104795190
import matplotlib.pyplot as plt


# 设置鼠标移动的交互事件
# 显示文本的标签
# 参数1,2:文本显示的横坐标和纵坐标
# 参数3：显示内容
# 参数fontsize:设置字号大小
# 参数bbox：设置文本框

text0 = plt.text(0,0,'xxx',fontsize=10,color='k',bbox=dict(facecolor='w',alpha=0.3))
line_x = plt.axhline(y=40,c='#999999',ls='--',lw=1)
line_y = plt.axvline(x=40,c='#999999',ls='--',lw=1)


def on_mouse(event):
    # print('on mouse...')
    try:
        x = int(np.round(event.xdata))
        y = int(np.round(event.ydata))
        # print(x,y)
        line_x.set_ydata(y)
        line_y.set_xdata(x)
        # 当前坐标的时间
        data = pub_datas[x]
        data = '日期：'+str(pub_datas[x])+'\n'+\
            '现存确诊：'+str(cn_diagnosisNum[x])+'\n'+\
            '现存疑似：'+str(cn_susNum[x])
        print(data)
        text0.set_text(data)
        text0.set_position((x,y))

    except Exception as e:
        # 鼠标移开，隐藏
        text0.set_position((-40, 0))
        line_x.set_ydata(-4000)
        line_y.set_xdata(-4000)
        print(e)
    # 把绘图动作实时反映在图形上
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_mouse)
plt.show()
# def on_key_press(event):
#     print(event.key)
#
# fig,ax = plt.subplots()
# fig.canvas.mpl_connect('key_press_event', on_key_press)
# plt.show()

# # 保存图片
# plt.savefig('中国疫情走势图.png')
# plt.show()
