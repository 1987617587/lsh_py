# author:lsh
# datetime:2020/4/29 16:08 
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

from sklearn.datasets import load_boston

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression, SGDRegressor

# 加载数据集
bst = load_boston()
# print(bst.DESCR)
#
# 分割数据集
x_train, x_test, y_train, y_test = train_test_split(bst.data, bst.target, test_size=0.25)
# 数据标准化处理
# 特征值
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train.reshape(-1,1))
x_test = std_x.transform(y_test.reshape(-1,1))
# 目标值
std_y = StandardScaler()
y_train = std_y.fit_transform(y_test.reshape(-1,1))
y_test = std_y.transform(y_test.reshape(-1,1))
# 估计其流程

lr = LinearRegression()
lr.fit(x_train,y_train)
pred_lr = lr.predict(x_test)
print('lr欲测值：',pred_lr)
# 查看回归系数
print(lr.coef_)
print('+'*66)

sgd = SGDRegressor()
sgd.fit(x_train,y_train)
pred_sgd = sgd.predict(x_test)

print('sgd欲测值：',pred_lr)
# 查看回归系数
print(sgd.coef_)
print('+'*66)