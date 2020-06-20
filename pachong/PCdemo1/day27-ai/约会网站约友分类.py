# author:lsh
# datetime:2020/4/29 11:08 
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
import pandas as pd
from sklearn.model_selection._split import train_test_split
from sklearn.neighbors.classification import KNeighborsClassifier
# K近邻分类器
# from sklearn.neighbors import KNeighborsClassifier
# 归一化
from sklearn.preprocessing import MinMaxScaler

# 加载数据
data_array = pd.read_csv('data/datingTestSet2.csv')
count = data_array.shape[0]
print('count:', count)
# 特征值
df_feature = data_array.iloc[:, 0:3]
# print(df_feature)
# 目标值
df_labels = data_array.iloc[:, 3]
print(df_labels)
# 数据集进行分割
# 按照惯例，需要对数据集进行分割，25%的样本用于测试，75%用于训练
x_train, x_text, y_train, y_text = train_test_split(df_feature, df_feature, test_size=0.25)

# 特征归一化处理
minmax = MinMaxScaler(feature_range=(0,1))
x_train = minmax.fit_transform(x_train)
x_text = minmax.transform(x_text)
# print(x_train)
# print(x_text)
# 模型检验
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_predict = knn.predict(x_text)
print(y_predict)
print(y_text)
score = knn.score(x_text,y_text)
print(score)


# 模型应用

user_type_ls = ['屌丝','文艺青年','高富帅']
while True:
    miles = float(input('飞行常客里程数：'))
    video = float(input('视频游戏时间比：'))
    ice_cream = float(input('每周消耗冰淇淋公升数：'))
    new_data = [[miles,video,ice_cream]]
    # 对传入的数据进行归一化处理
    new_data = minmax.transform((new_data))


    result = knn.predict(new_data)

    print(result)
    print(user_type_ls[result[0]])
