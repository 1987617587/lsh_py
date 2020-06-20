# level 2:
# 案例：搜狗微信爬虫(bs4):
# https://weixin.sogou.com/
# https://weixin.sogou.com/weixin?type=2&query=python&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1581585228962&lkt=0%2C0%2C0&p=40040108
# 搜索python，爬取标题，连接，文章概要，来源，发表时间



import pymongo

# 创建MangoDB连接
try:
    # 创建MongoClient对象 建立和MongoDB的连接
    client = pymongo.MongoClient('localhost', 27017)
    # 指定数据库名字
    db = client['db_pachong']
    # 指定集合的名称
    collec = db.yiliao
except Exception as e:
    print(e)

# 页面请求
import os
import re

import requests
# 数据提取
from bs4 import BeautifulSoup
from lxml import etree
# 数据存储
import csv
# 打开文件，避免空行
import codecs
# 设置爬取的随机延迟
import time
import random

from day02.requests_xundaili import down


# 通过函数展示注意操作步骤
# 设定UA
def get_ua():
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    return headers


# 获取
def parse_album_list(url):
    response = requests.get(url, headers=get_ua())
    # response = down(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取相册列表（ul有多个class 使用.ml.mla.cl表示）
    ls = soup.select('div.txt-box')
    print(f'album len:{len(ls)}')
    for each in ls:
        title = each.select_one('h3 a').get_text()
        print("title:",title)
        album_url = each.select_one('h3 a').attrs['href']
        # 未解决编码问题 TODO
        print("album_url:",album_url)
        abstract = each.select_one('p').get_text()
        print("abstract:",abstract)

        source = each.select_one('div.s-p a.account').get_text()
        print("source:", source)
        pub_time = each.select_one('span.s2 script').get_text()
        print("pub_time:", pub_time)
        # 使用re获取时间戳
        pub_time = re.findall(r'(\d+)', pub_time)[0]
        print(re.findall(r'(\d+)', pub_time)[0])
        # 使用time 时间戳转换

        timeArray = time.localtime(int(pub_time))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)
        # # 抛弃英文分类
        # if "html" in album_url:
        #     print("+" * 30)


if __name__ == '__main__':
    parse_album_list("https://weixin.sogou.com/weixin?type=2&query=python&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1581585228962&lkt=0%2C0%2C0&p=40040108")



