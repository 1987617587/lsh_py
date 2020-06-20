# author:lsh
# datetime:2020/4/26 20:24 
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
买商标网爬虫
http://www.mp.ink/tgmp2?k=439642&bd_vid=8250654376519157897
爬取出售商标的名称，编号，类别，专用期限，注册范围，商标图片
'''
import re
from lxml import etree

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
base_url = 'http://www.mp.ink'

i =1
def get_list(url):
    response = requests.get(url, headers=headers)
    # print(response.text)

    html = etree.HTML(response.text)
    ls = html.xpath('//li/a[@class="img-container"]')
    print(f'len:{len(ls)}')
    for each in ls:
        detail_url = base_url + each.xpath('./@href')[0]
        print(f'detail_url:{detail_url}')
        get_detail(detail_url)
        print('+' * 22)

    max_page = html.xpath('//input[@id="pageNum"]/@value')[0]
    print(max_page)
    global i
    i+=1

    if i <= int(max_page):
        next_page_url = 'http://www.mp.ink/ajax_tg_brand/'+str(i)+'?&tg=tgmp2'
        print(next_page_url)
        get_list(next_page_url)
        time.sleep(random.random())


def get_detail(url):
    response = requests.get(url, headers=headers)
    # print(response.text)

    html = etree.HTML(response.text)
    # 爬取出售商标的名称，编号，类别，专用期限，注册范围，商标图片
    title = html.xpath('//div[@class="d_top_rt_left"]/text()')[0]
    print(f'title:{title}')
    nums = html.xpath('//div[@class="item view_sn"]/span/text()')[0]
    print(f'nums:{nums}')
    category = html.xpath('//div[@class="item "]/span/text()')[0]
    print(f'category:{category}')
    special_term = html.xpath('//div[@class="item "]/span/text()')[1]
    print(f'special_term:{special_term}')
    registration_scope = html.xpath('//div[@class="item "]/span/text()')[3]
    print(f'registration_scope:{registration_scope}')
    img_url = html.xpath('//div[@class="d_top_lt_img"]/img/@src')[0]
    # print(f'img_url:{img_url}')
    down_photo(img_url,nums)
    print('+'*200)
    time.sleep(random.random())


# 图片下载
def down_photo(img_url,nums):
    print(f'img_url:{img_url}')

    img_response = requests.get(img_url, headers=headers)
    with open('images/' + nums + ".jpg", "wb")as file:
        # 字节流
        file.write(img_response.content)


if __name__ == '__main__':
    url = 'http://www.mp.ink/ajax_tg_brand/1?&tg=tgmp2'
    get_list(url)
