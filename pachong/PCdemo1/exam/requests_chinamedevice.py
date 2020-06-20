# level 3:
# 案例：豆瓣图书爬虫(bs4)
# https://book.douban.com/tag/?icn=index-nav
# 按类别爬取图书的名称，url，作者，译者，出版社，出版日期，价格，评论数，评分，简介，类别，封面链接
# 保存到mysql数据库
#


# 页面请求
import pymysql
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

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

url = "https://www.tvmao.com/drama/aG0gXGRh/episode"
# url = "https://www.tvmao.com/drama/aG0gXGRh/episode/0-2"

try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
    cur = conn.cursor()
except Exception as e:
    print(e)

def get_text(url):
    response = requests.get(url, headers=headers)
    html = response.text
    print(html)
    html = etree.HTML(html)
    # print(html)
    # 分析结果，编写xpath匹配表达式
    title = html.xpath('//p[@class="epi_t"]/text()')[0]
    print(title)
    content = html.xpath('//article[@class="clear epi_c"]/p/text()')
    content= ''.join(content)
    print(content)
    # 数据存储
    strsql = 'insert into dianshiju VALUES (0,%s,%s)'
    params = [title, content]
    cur.execute(strsql, params)
    conn.commit()
    # 翻页
    next_page = html.xpath('//div[@class="alignct"]//a/@href')[-1]
    print(next_page)
    next_page_text = html.xpath('//div[@class="alignct"]//a/text()')[-1]
    print(next_page_text)
    time.sleep(random.random())
    if '下一集' in next_page_text:
        url = 'https://www.tvmao.com'+next_page
        get_text(url)




if __name__ == '__main__':
    get_text(url)
    cur.close()
    conn.close()
