import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
}

# url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback21971&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1585894236331'

# 把上面路由优化，修改参数，进行多页爬取
pageCount = 1
url = 'http://query.sse.com.cn/security/stock/getStockListData2.do'

# for page in range(5):
page = 0
while page<= pageCount:
    page+=1
    print(f'page:{page}')

    params = {
        'jsonCallBack': 'jsonpCallback21971',
        'isPagination': 'true',
        'stockCode': '',
        'csrcCode': '',
        'areaName': '',
        # 'stockType': 1,
        # 'pageHelp.cacheSize': 1,
        # 'pageHelp.beginPage': 1,
        # 'pageHelp.pageSize': 25,
        # 'pageHelp.pageNo': 1,
        # '_': '1585894236331', # 时间戳 time.time()*1000
        # 对参数进行修改，循环使用
        'stockType': 1,
        'pageHelp.cacheSize': 1,
        'pageHelp.beginPage': page,
        'pageHelp.pageSize': 25,
        'pageHelp.pageNo': page,
        '_': int(time.time()*1000),  # 时间戳 time.time()*1000

    }
    response = requests.get(url, params=params, headers=headers)
    html = response.text
    # print(html)
    pat = re.compile(r'\((.*?)\)')
    html = pat.search(html).group(1)
    data = json.loads(html)
    if pageCount == 1:
        # 数据中返回的有页数
        pageCount = int(data['pageHelp']['pageCount'])

    ls = data['pageHelp']['data']
    print(f'len{len(ls)}')

    for each in ls:
        LISTING_BOARD = each['LISTING_BOARD']
        print(LISTING_BOARD)
        COMPANY_ABBR = each['COMPANY_ABBR']
        print(COMPANY_ABBR)

        COMPANY_CODE = each['COMPANY_CODE']
        print(COMPANY_CODE)

        LISTING_DATE = each['LISTING_DATE']
        print(LISTING_DATE)
        print('==' * 20)
    time.sleep(random.random())
