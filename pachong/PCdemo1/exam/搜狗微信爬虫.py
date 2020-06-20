# 1:
# 搜狗微信爬虫
# 获取搜索关键字分别为微星，机械革命，炫龙，机械师，神州五个笔记本品牌的前10页微信文章信息，字段包含（标题，文章链接，简介内容，来源，发布时间【时间格式为yyyy-mm-dd，年份月份分期用-连接】），信息保存在MongoDB中。
# https://weixin.sogou.com/weixin?type=2&query=%E7%82%AB%E9%BE%99&ie=utf8&s_from=input&_sug_=y&_sug_type_=
import datetime

import requests
# 数据提取
from bs4 import BeautifulSoup

# 设置爬取的随机延迟
import time
import random
import pymongo


# 创建MangoDB连接
def get_collection():
    try:
        # 创建MongoClient对象 建立和MongoDB的连接
        client = pymongo.MongoClient('localhost', 27017)
        # 指定数据库名字
        db = client['db_pachong']
        # 指定集合的名称
        # collec = db.yiliaoqixie
        collec = db['sougouweix']
        return collec
    except Exception as e:
        print(e)
    return None


# 页面请求
import os
import re


# 获取指定页面内容
def requests_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    response = requests.get(url, headers=headers)
    # html = response.text
    # print(html)
    soup = BeautifulSoup(response.text, 'lxml')
    return (url, soup)


# 字段包含（标题，文章链接，简介内容，来源，发布时间【时间格式为yyyy-mm-dd，年份月份分期用-连接】），信息保存在MongoDB中。


def parse_catetory_list(url):
    currcent_url, soup = requests_url(url)

    ls = soup.select('ul.news-list > li > div.txt-box ')
    print(f' len:{len(ls)}')
    for each in ls:
        title = each.select_one('h3 > a').get_text()
        print(f'title:{title}')
        title_url = each.select_one('h3 > a').get('href')
        print(f'title_url:{title_url}')
        introduction = each.select_one('p').get_text()
        print(f'introduction:{introduction}')
        source = each.select_one('div.s-p > a.account').get_text()
        print(f'source:{source}')
        pub_date = each.select_one('span.s2 > script').get_text()
        pub_date = re.search(r'\d+', pub_date).group()
        pub_date = time.strftime("%Y-%m-%d", time.localtime(int(pub_date)))
        print(f'pub_date:{pub_date}')

        # 存储
        data = {
            'title': title,
            'title_url': title_url,
            'introduction': introduction,
            'source': source,
            'pub_date': pub_date,
        }
        collec.insert(data)

    time.sleep(random.random())


if __name__ == '__main__':
    collec = get_collection()
    titles = ['微星', '机械革命', '炫龙', '机械师', '神州']
    for title in titles:
        for i in range(10):
            url = 'https://weixin.sogou.com/weixin?query={}&_sug_type_=&s_from=input&_sug_=y&type=2&page={}&ie=utf8'.format(
                title, i)
            parse_catetory_list(url)
