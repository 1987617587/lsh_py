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

url = "https://book.douban.com/tag/?icn=index-nav"

try:
    conn = pymysql.connect(host='192.168.1.119', port=3306, user='lsh', password='123456', db='books')
    cur = conn.cursor()
except Exception as e:
    print(e)

# 使用之前封装好的讯代理
response = down(url=url)

# html = response.content.decode(response.apparent_encoding)
html = response.text
print(html)
# 提取数据
soup = BeautifulSoup(html, 'lxml')
ls = soup.select('table.tagCol  td ')
print('len:', len(ls))
base_url = 'https://book.douban.com'
for item in ls:
    detail_url = base_url + item.select_one('a').get('href')
    # 请求章节的详情页面
    print("准备进入详情", detail_url)
    html = down(detail_url).text
    # bs4做解析
    detail_soup = BeautifulSoup(html, 'lxml')
    # 类别
    category = detail_soup.select_one('div#content > h1').get_text()
    category = category[7:]
    print('title:', category)
    # 书籍列表
    books = detail_soup.select('div#content  li.subject-item')
    print(books, len(books))
    print("+" * 20)

    for book in books:
        # book_name = book.select_one('div#content  li.subject-item h2 a').get('title')
        book_name = book.select_one('h2 a').get('title')
        print(book_name)
        book_url = book.select_one('h2 a').get('href')
        # book_author = book.select_one('div.pub').get_text()  此处出现问题，有空行
        # 此处未作切片 [美] 特德·姜 / 耿辉、Ent、李克勤、姚向辉 / 译林出版社 / 2019-12 / 42
        book_author = book.select_one('div.pub')
        book_author = book_author.prettify()
        book_author = book_author.replace('<div class="pub">', '')
        book_author = book_author.replace('</div>', '')
        book_author = book_author.replace('\n\n \n\n', '\n')
        book_author = book_author.strip()
        print(book_author)
        # 评分
        book_star = book.select_one('span.rating_nums').get_text()
        # book_star = book_star.prettify()
        print(book_star)
        # 评论数
        book_readnums = book.select_one('span.pl').get_text()
        # book_readnums = book_readnums.prettify()
        # book_readnums = book_readnums.replace('\n\n \n\n', '\n')
        print(book_readnums)
        # 简介
        book_p = book.select_one('p').get_text()
        print("简介:", book_p)
        # 图书封面链接
        bookphoto_url = book.select_one('div.pic a img').get('src')
        print("封面链接:", book_url)
        print("=" * 20)
        # 3、数据存储
        # 尝试连接数据库（ubuntu下）

        strsql = 'insert into lianjia VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = [category, detail_url, book_name, book_url, book_author, book_star, book_readnums, book_p,
                  bookphoto_url]
        cur.execute(strsql, params)
        conn.commit()
    cur.close()
    conn.close()
