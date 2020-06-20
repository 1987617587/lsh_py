# author:lsh
# datetime:2020/4/28 17:13 
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
import json
import random
import time

''' 
level 2:
案例：全国公共资源交易平台爬虫：
爬取公告名称，链接，发布日期，来源平台
http://deal.ggzy.gov.cn/ds/deal/dealList.jsp
'''

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'Cookie': 'JSESSIONID=013b6ef61fd07f84c2c3d4e359aa; JSESSIONID=013b50cca9fa7a624e780b28d396; insert_cookie=71170129; JSESSIONID=013b6ef61fd07f84c2c3d4e359aa'
}

# 爬取300页
for i in range(1, 301):

    TIMEEND_SHOW = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    print(TIMEEND_SHOW)
    data = {
        'TIMEBEGIN_SHOW': '2020-04-19',
        'TIMEEND_SHOW': TIMEEND_SHOW,
        'TIMEBEGIN': '2020-04-19',
        'TIMEEND': TIMEEND_SHOW,
        'SOURCE_TYPE': 1,
        'DEAL_TIME': '02',
        'DEAL_CLASSIFY': '00',
        'DEAL_STAGE': '0000',
        'DEAL_PROVINCE': '0',
        'DEAL_CITY': '0',
        'DEAL_PLATFORM': '0',
        'BID_PLATFORM': '0',
        'DEAL_TRADE': '0',
        'isShowAll': '1',
        # 'PAGENUMBER': 1,  # 页码
        'PAGENUMBER': i,  # 页码

    }
    url = 'http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp'

    response = requests.post(url, data=data, headers=headers)
    # print(response.text)
    data = json.loads(response.text)['data']
    # print(data)

    with codecs.open('ggzy.csv', 'a', encoding='utf-8') as file:
        wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
        if i == 1:
            wr.writerow(['title', 'detail_url', 'timeShow', 'platformName'])

    for each in data:
        # 爬取公告名称，链接，发布日期，来源平台
        title = each['title']
        print(f'title:{title}')

        detail_url = each['url']
        print(f'detail_url:{detail_url}')
        timeShow = each['timeShow']
        print(f'timeShow:{timeShow}')
        platformName = each['platformName']
        print(f'platformName:{platformName}')
        print('=' * 200)
        # 数据存储
        with codecs.open('ggzy.csv', 'a', encoding='utf-8') as file:
            wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
            # if i == 1 and each['classify']=='01':
            #     wr.writerow(['title', 'detail_url', 'timeShow','platformName'])
            # else:
            wr.writerow([title, detail_url, timeShow,platformName])

    # 翻页设定延迟
    time.sleep(random.random() + 0.5)
