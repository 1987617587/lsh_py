#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import re
import requests
from bs4 import BeautifulSoup
import execjs
import time
import random
import json


def anti_value(sess):
    '''
    获取cookie中antipas参数
    :return:
    '''
    url = 'https://www.guazi.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    respone = sess.get(url, headers=headers)
    content = respone.content.decode(respone.apparent_encoding)
    # print(content)
    pat = re.compile(r'<script.*?>(.*?)</script>', re.M | re.S)
    js = pat.search(content).group(1)
    js = js.replace(r"xredirect(name,value,url,'https://');", '')
    pat = re.compile(r"value=anti\('(.*?)','(.*?)'", re.M | re.S)
    params = pat.findall(js)[0]
    print('params:', params)
    ctx = execjs.compile(js)
    antipas = ctx.call('anti', params[0], params[1])
    print(antipas)
    sess.cookies.set('antipas', antipas)
    return sess


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        # 'Upgrade-Insecure-Requests': 1
    }
    sess = requests.Session()
    sess.headers = headers
    sess = anti_value(sess)
    url = 'https://www.guazi.com/qd/buy/'
    page_num_max = 1
    page = 1
    while True:
        print('page:', page)
        response = sess.get(url)
        html = response.content.decode(response.apparent_encoding)
        # print(html)
        html = BeautifulSoup(html, 'lxml')
        if page_num_max == 1:
            print('mlen:', len(html.select('ul.pageLink.clearfix')))
            page_num_max = html.select('ul.pageLink.clearfix > li > a')[8].get_text()
            page_num_max = int(page_num_max)
            print('page_num_max:', page_num_max)
        # 汽车的列表
        ls = html.select('ul.carlist.clearfix.js-top > li > a')
        print('len:', len(ls))
        base_url = 'https://www.guazi.com'
        for each in ls:
            detail_url = base_url + each.get('href')
            print('detail_url:', detail_url)
            response_detail = sess.get(detail_url)
            html_detail = response_detail.text
            html_detail = BeautifulSoup(html_detail, 'lxml')
            # 标题
            title = html_detail.select_one('h2.titlebox').contents[0].string.strip()
            print('title:', title)
            # 里程数
            km = html_detail.select_one('ul.assort.clearfix > li.two > span').get_text().strip()
            print('km:', km)
            # 排气量
            emissions = html_detail.select_one('ul.assort.clearfix > li.three > span').get_text().strip()
            print('emission:', emissions)
            # 变速箱
            transimission = html_detail.select_one('ul.assort.clearfix > li.last > span').get_text().strip()
            # 价格
            price = html_detail.select_one('span.price-num').get_text().strip()
            print('price:', price)
            print('=' * 200)
            with open('data.json', 'a', encoding='utf-8') as file:
                data = {
                    'title': title,
                    'detail_url': detail_url,
                    'km': km,
                    'emissions': emissions,
                    'transimission': transimission,
                    'price': price
                }
                data = json.dumps(data) +'\n'
                file.write(data)

        time.sleep(random.random())
        page += 1
        url = 'https://www.guazi.com/qd/buy/o{}/#bread'.format(page)
        if page > page_num_max:
            break
