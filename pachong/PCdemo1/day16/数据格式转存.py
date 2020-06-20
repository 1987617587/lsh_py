# author:lsh
# datetime:2020/4/14 14:39 
'''
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
                                                                                                     
            '''
import pandas as pd
import csv
import codecs
import json

# csv===> excel
# df = pd.read_csv('./data/a.csv',encoding='utf-8')
# df.to_excel('./data/a.xlsx',sheet_name='csv转excel')

# excel ===> csv
# df_xls = pd.read_excel('./data/a.xlsx',index_col=0)
# df_xls.to_csv('./data/b.csv',encoding='utf-8')
# csv ===>json
df_csv = pd.read_csv('./data/a.csv',encoding='utf-8')
count = df_csv.shape[0]  # 获取行数
with open('./data/b.json','w',encoding='utf-8') as file:
    for i in range(count):
        d = {
            '0':df_csv.iloc[i,0],
            '1':df_csv.iloc[i,1],
            '2':df_csv.iloc[i,2],
        }
        file.write(json.dumps(d)+'\n')
# json ===>csv
with open('./data/a.json','w',encoding='utf-8') as file1:
    with open('./data/c.csv', 'w', encoding='utf-8') as file2:
        wr = csv.writer(file2)
        wr.writerow(['1','2','3'])
        line = file1.readline()
        while line:
            d = json.loads(line)
            wr.writerow([d['1'],d['2'],d[3]])