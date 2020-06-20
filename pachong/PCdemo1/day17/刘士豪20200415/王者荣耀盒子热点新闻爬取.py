# author:lsh
# datetime:2020/4/15 16:58 
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
import pymysql
from lxml import etree

'''
案例：王者荣耀盒子热点新闻爬虫
爬取热点新闻标题，封面图片链接，详情id，来源，发布时间，新闻内容
存储mysql数据库
'''

import os
import re

import requests
import time
import random
import json

try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
    cur = conn.cursor()
except Exception as e:
    print(e)

headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
}
base_url = 'http://gamehelper.gm825.com'


def get_news(pn):
    if pn == 1:
        url = '/wzry/hot/information?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=12A84CF38D43ACBCB630B0F61EA6C6B7&ovr=5.1.1&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=Q%2Ft3pkcmtbETmZ7I%2BI%2FHpA%3D%3D&info_ms=Q%2F3EH69Etqj3fT9W9HrrMw%3D%3D&info_ma=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&mno=0&info_la=qma3PGAUEipKo9jsdzK7fA%3D%3D&info_ci=qma3PGAUEipKo9jsdzK7fA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&os_level=22&os_id=80fa5b720bca1407&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=b720bca140780fa5 HTTP/1.1'
    else:
        url = f'/wzry/news/list?pn={str(pn)}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=12A84CF38D43ACBCB630B0F61EA6C6B7&ovr=5.1.1&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=Q%2Ft3pkcmtbETmZ7I%2BI%2FHpA%3D%3D&info_ms=Q%2F3EH69Etqj3fT9W9HrrMw%3D%3D&info_ma=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&mno=0&info_la=qma3PGAUEipKo9jsdzK7fA%3D%3D&info_ci=qma3PGAUEipKo9jsdzK7fA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&os_level=22&os_id=80fa5b720bca1407&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=b720bca140780fa5 HTTP/1.1'

    # response = requests.get(url, params=params, headers=headers)
    response = requests.get(base_url + url, headers=headers)

    # json格式
    data = response.json()

    # print(data)
    if 'news_list' in data:
        news_list = data['news_list']
    else:
        news_list = data['list']

    for news in news_list:
        title = news['title']
        cover = news['cover']
        detail_id = news['detail_id']
        source = news['source']
        ctime = news['ctime']
        pud_time = time.strftime("%Y-%m-%d", time.localtime(int(ctime)))
        print(f'title:{title}')
        print(f'detail_id:{detail_id}')
        print(f'source:{source}')
        print(f'cover:{cover}')
        print(f'pud_time:{pud_time}')
        print('+' * 100)
        get_detail_text(detail_id)
        time.sleep(random.random())
        # break
        strsql = 'insert into wzry_news VALUES(0,%s,%s,%s,%s,%s,%s)'
        content = ''
        params = [title, cover, detail_id, source, pud_time, content]
        cur.execute(strsql, params)
        conn.commit()
    time.sleep(random.random())


#     GET /wzry/article/54449.html?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010 HTTP/1.1
def get_detail_text(detail_id):
    url = '/wzry/article/' + str(
        detail_id) + '.html?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010 HTTP/1.1'
    response = requests.get(base_url + url, headers=headers)
    html = response.text
    # print(html)
    html = etree.HTML(html)
    content = html.xpath('//div[@class="main_content"]//p//text()')
    content = ''.join(content)
    content = ''.join(content.split())
    print(content,type(content))
    print('=' * 100)
    # strsql = "SELECT * FROM wzry_news WHERE detail_id = %s" % (detail_id)
    # strsql = "UPDATE wzry_news SET content = '%s' WHERE detail_id = '%s'" % (content,detail_id)
    strsql = f"UPDATE wzry_news SET content = '{str(content)}' WHERE detail_id = {detail_id}"

    cur.execute(strsql)
    conn.commit()


if __name__ == '__main__':
    # 爬取5页新闻
    for i in range(5):
        get_news(i)

    cur.close()
    conn.close()
