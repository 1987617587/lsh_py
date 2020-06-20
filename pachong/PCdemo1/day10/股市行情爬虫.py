import requests
import demjson
import pymysql
import time
import random
import math
import re

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
cur = conn.cursor()
count_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount'
data_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'

type_ls = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'sh_z', 'sz_z']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
pat_1 = re.compile(r'(\d+)')
size = 40
for type in type_ls:
    # 请求指定类别股票数量
    param1 = {
        'data': type
    }
    html = requests.get(count_url, params=param1, headers=headers).text
    count = int(pat_1.search(html).group(1))
    page_count = math.ceil(count / size)
    print('count:', count, 'page_count:', page_count)
    # 请求不同类别不同页码的股票信息
    for page in range(1, page_count + 1):
        param2 = {
            'page': page,
            'num': 40,
            'sort': 'symbol',
            'asc': 1,
            'data': type,
            'symbol': '',
            '_s_r_a': 'init',
        }
        print('type:', type, 'page:', page)
        html = requests.get(data_url, params=param2, headers=headers).text
        # print(html)
        ls = demjson.decode(html)
        for each in ls:
            symbol = each['symbol']
            print('symbol:', symbol)
            code = each['code']
            print(f'code:{code}')
            name = each['name']
            print('name:', name)
            trade = each['trade']
            print('trade:', trade)
            pricechange = each['pricechange']
            print('pricechange:', pricechange)
            changepercent = each['changepercent']
            print('changepercent:', changepercent)
            buy = each['buy']
            print('buy:', buy)
            sell = each['sell']
            print('sell:', sell)
            settlement = each['settlement']
            print(f'settlement:{settlement}')
            open = each['open']
            print('open:', open)
            high = each['high']
            print('high:', high)
            low = each['low']
            print('low:', low)
            volume = each['volume']
            print('volume:', volume)
            amount = each['amount']
            print('amount:', amount)
            ticktime = each['ticktime']
            print('ticktime:', ticktime)
            print('=' * 200)
            strsql = 'insert into finance VALUES(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            params = [symbol, code, name, trade, pricechange, changepercent, buy, sell, settlement, open, high, low]
            cur.execute(strsql, params)
            conn.commit()
        time.sleep(random.random())

cur.close()
conn.close()