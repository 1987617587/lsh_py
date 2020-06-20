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
import demjson
import pymysql
import time
import random
import math
import re

import requests
from lxml import etree
from gshq_work import crawl


class Clinet:
    def __init__(self):
        self.urls = []
        self.base_url = 'https://www.tianqi.com'
        self.count_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount'
        self.data_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'
        self.type_ls = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'sh_z', 'sz_z']

    def get_urls(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }

        pat_1 = re.compile(r'(\d+)')
        size = 40
        for type in self.type_ls:
            # 请求指定类别股票数量
            param1 = {
                'data': type
            }
            html = requests.get(self.count_url, params=param1, headers=headers).text
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

                self.urls.append(( self.data_url, param2))

    def task_manage(self):
        '''
        把任务添加到任务队列中
        :return:
        '''
        for item in self.urls:
            crawl.delay(item[0], item[1])


if __name__ == '__main__':
    client = Clinet()
    client.get_urls()
    client.task_manage()


