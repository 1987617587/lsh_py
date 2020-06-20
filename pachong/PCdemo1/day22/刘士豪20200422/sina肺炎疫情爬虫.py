# author:lsh
# datetime:2020/4/22 19:53 
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
import codecs
import csv
import re
import time

'''
sina肺炎疫情爬虫：
爬取肺炎数据，保存csv
*https://news.sina.cn/zt_d/yiqing0121
*绘制全国疫情累计趋势图
'''

import requests
import json
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}
# ?_=1587556476084&callback=dataAPIData
c_time = time.time()
# 1587622751.4823017
# 1587556476.084
params = {
    '_': float(c_time*1000),
    'callback': 'dataAPIData'
}

url = 'https://gwpre.sina.cn/interface/fymap2020_data.json'

response = requests.get(url, headers=headers,params=params)

html = response.text
# print(html)
pat = re.compile(r'dataAPIData\((.*?)\)', re.M | re.S)
html = pat.search(html).group(1)
data = json.loads(html)['data']
# print(data)
historylist = data['historylist']
print(historylist)

for each in historylist:
    pub_date = each['date']
    if pub_date == '03.18':
        break
    cn_conNum = each['cn_conNum']
    cn_deathNum = each['cn_deathNum']
    cn_cureNum = each['cn_cureNum']
    # print(cn_conNum,cn_deathNum,cn_cureNum)
    # cn_conNum-cn_deathNum-cn_cureNum = 现存确诊人数
    cn_diagnosisNum = int(cn_conNum) - (int(cn_deathNum) + int(cn_cureNum))
    cn_susNum = each['cn_susNum']  # 现存疑似

    print(pub_date, cn_diagnosisNum, cn_susNum)
    print('=' * 22)
    # 数据存储
    with codecs.open('epidemic_information.csv', 'a', encoding='utf-8') as file:
        wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
        wr.writerow([pub_date, cn_diagnosisNum, cn_susNum])
