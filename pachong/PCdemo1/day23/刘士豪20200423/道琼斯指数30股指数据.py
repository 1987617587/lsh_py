# author:lsh
# datetime:2020/4/22 19:34 
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

'''
案例：
http://money.cnn.com/data/dow30
编写爬虫，下载道琼斯指数30股指数据 代码code，名称name，最后交易价格tradePrice
保存为csv文件
'''
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}
url = 'https://money.cnn.com/data/dow30/'

response = requests.get(url, headers=headers)

html = etree.HTML(response.text)
# 不带表头
ls = html.xpath('//table[@class="wsod_dataTable wsod_dataTableBig"]//tr')[1:]
# ls = html.xpath('//table[@class="wsod_dataTable wsod_dataTableBig"]//tr')
print(f'len{len(ls)}')
i= 0
for each in ls:
    code = each.xpath('.//a[@class="wsod_symbol"]/text()')[0]
    name = each.xpath('.//td[@class="wsod_firstCol"]/span/text()')[0]
    tradePrice = each.xpath('.//td[@class="wsod_aRight"]/span/text()')[0]
    print(code,name,tradePrice)
    # 数据存储
    with codecs.open('money.csv', 'a', encoding='utf-8') as file:
        wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
        if i==0:
            wr.writerow(['code', 'name', 'tradePrice'])
        else:
            wr.writerow([code, name, tradePrice])
        i+=1