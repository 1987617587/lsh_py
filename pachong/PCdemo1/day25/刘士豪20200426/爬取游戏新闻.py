# author:lsh
# datetime:2020/4/26 19:56 
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
import random
import time

'''
level 1:
爬取有关游戏新闻标题，发表时间，封面链接，新闻内容
http://www.199it.com/archives/tag/sensor-tower
'''
import re
from lxml import etree

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def get_list(url):
    response = requests.get(url, headers=headers)
    print(response.text)
    # pat_price = re.compile(r'(￥\d+)')
    # print(pat_price.search(response.text)[0])
    #
    html = etree.HTML(response.text)
    ls = html.xpath('//h2[@class="entry-title"]/a')
    print(f'len:{len(ls)}')
    for each in ls:
        title = each.xpath('./@title')[0]
        # print(f'title:{title}')
        detail_url = each.xpath('./@href')[0]
        # print(f'detail_url:{detail_url}')
        get_detail(detail_url)
        print('+' * 22)

    next_page_url = html.xpath('//a[@class="next page-numbers"]')
    if next_page_url:
        next_page_url = next_page_url[0].xpath('./@href')[0]
        print(next_page_url)

        get_list(next_page_url)
        time.sleep(random.random())
    else:
        print('后面没有了')


def get_detail(url):
    response = requests.get(url, headers=headers)
    print(response.text)

    html = etree.HTML(response.text)
    # 爬取有关游戏新闻标题，发表时间，封面链接，新闻内容
    title = html.xpath('//h1[@class="entry-title"]/text()')[0]
    print(f'title:{title}')
    pub_date = html.xpath('//li[@class="post-time"]/time/text()')[0]
    print(f'pub_date:{pub_date}')
    detail_url = url
    print(f'detail_url:{detail_url}')

    detail_text = html.xpath('//div[@class="article-summary"]/p//text()')
    detail_text = ''.join(detail_text)
    print(f'detail_text:{detail_text}')


if __name__ == '__main__':
    url = 'http://www.199it.com/archives/tag/sensor-tower'
    get_list(url)
