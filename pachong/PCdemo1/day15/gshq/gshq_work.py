# author:lsh
# datetime:2020/4/13 17:50 
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
import requests
from celery import Celery
import demjson

uri1 = 'redis://@127.0.0.1:6379/5' # 存储执行的结果
uri2 = 'redis://@127.0.0.1:6379/6' # 存储任务队列
app = Celery('gshq_work',backend=uri1,broker=uri2)


@app.task
def crawl(data_url,params):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }

    html = requests.get(data_url, params=params, headers=headers).text
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
        return [symbol, code, name, trade, pricechange, changepercent, buy, sell, settlement, open, high, low]






