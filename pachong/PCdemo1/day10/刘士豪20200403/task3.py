'''

股市行情爬虫
http://vip.stock.finance.sina.com.cn/mkt/#sh_a
爬取沪深两市A股，B股，深市债券，沪市债券信息，
保存到myssql数据库

'''

import demjson
import re
import time, random
import requests
from lxml import etree
import pymysql


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Cookie': 'browserid=1583519136134043099; timezoneOffset=28800,0; _ga=GA1.2.286001437.1585136894; recentapps=%7B%2212210%22%3A1585139106%7D; steamCountry=CN%7C5f5d50facb921b2c63f83bc655663d9b; sessionid=381c33614d8012f31c1256e5; _gid=GA1.2.1098869448.1585911359; app_impressions=346110@1_7_7_globaltopsellers_150_1|578080@1_7_7_globaltopsellers_150_1|782330@1_7_7_globaltopsellers_150_1|1100600@1_7_7_globaltopsellers_150_1|976730:1064220:1064221:1064270:1064271:1064272:1064273@1_7_7_globaltopsellers_150_1|952060@1_7_7_globaltopsellers_150_1|261550@1_7_7_globaltopsellers_150_1',
    'Referer': 'https://store.steampowered.com/search/?os=win&filter=globaltopsellers'
}
node_list = ['sh_a','sh_b','sz_a','sz_b']
# url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=40&sort=symbol&asc=1&node=sh_a&symbol=&_s_r_a=init'
url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'
# 爬取的股市
for node in node_list:
    # 加入循环，多页获取
    # for page in range(1,5):
    page = 1
    while True:
        print(f"page:{page}")

        params = {
            'page': page,
            'num': 40,
            'sort': 'symbol',
            'asc': 1,
            'data': node,
            'symbol': '',
            '_s_r_a': 'init',

        }
        response = requests.get(url, params=params, headers=headers).text
        data = demjson.decode(response)

        print(f'len:{len(data)}')

        for each in data:
            symbol = each['symbol']
            print(f'symbol:{symbol}')

            code = each['code']
            print(f'code:{code}')

            name = each['name']
            print(f'name:{name}')

            trade = each['trade']
            print(f'trade:{trade}')

            pricechange = each['pricechange']
            print(f'pricechange:{pricechange}')

            changepercent = each['changepercent']
            print(f'changepercent:{changepercent}')

            buy = each['buy']
            print(f'buy:{buy}')
            sell = each['sell']
            print(f'sell:{sell}')

            settlement = each['settlement']
            print(f'settlement:{settlement}')

            open = each['open']
            print(f'open:{open}')

            high = each['high']
            print(f'high:{high}')

            low = each['low']
            print(f'low:{low}')

            volume = each['volume']
            print(f'volume:{volume}')

            amount = each['amount']
            print(f'amount:{amount}')
            ticktime = each['ticktime']
            print(f'ticktime:{ticktime}')

            per = each['per']
            print(f'per:{per}')

            pb = each['pb']
            print(f'pb:{pb}')

            mktcap = each['mktcap']
            print(f'mktcap:{mktcap}')
            nmc = each['nmc']
            print(f'nmc:{nmc}')
            turnoverratio = each['turnoverratio']
            print(f'turnoverratio:{turnoverratio}')
            print('=' * 33)
            # 可以存储数据了
            try:
                conn = pymysql.connect(host="localhost", port=3306, user='root', password='123456',
                                            db='lshmysql', charset='utf8')
                cur = conn.cursor()


                # strsql = "INSERT INTO FINANCE(0,%s, %s, %s, %s, %s , %s, %s, %s, %s , %s, %s, %s)"
                strsql = 'insert into finance VALUES (0,%s, %s, %s, %s, %s , %s, %s, %s, %s , %s, %s, %s)'

                params = (symbol, code, name, trade, pricechange, changepercent, buy, sell, settlement, open, high, low)
                cur.execute(strsql, params)
                conn.commit()

            except Exception as e:
                print("链接数据库失败", e)



        page += 1
        time.sleep(random.random()+1)
        # 一直循环获取到该页面数量不足设定值40，说明信息爬取完毕
        if len(data) < 40:
            break
