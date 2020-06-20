#
# 案例：steam游戏爬虫（bs4）
# https://store.steampowered.com/search/?os=win&filter=globaltopsellers
# 爬取游戏名称，链接，发布日期，价格，封面链接

# 页面请求
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

url = "https://store.steampowered.com/search/?os=win&filter=globaltopsellers"

# 使用之前封装好的讯代理
response = down(url=url)

# html = response.content.decode(response.apparent_encoding)
html = response.text
print(html)
# 提取数据
soup = BeautifulSoup(html, 'lxml')
ls = soup.select('div.responsive_search_name_combined ')
print('len:', len(ls))
li_nums = 0
for item in ls:
    # 游戏名称
    title = item.select_one('span.title').get_text()
    print('title:', title)
    # 链接
    urls = soup.select('div#search_resultsRows a')
    url_nums = 0
    # 利用循环对应链接
    for each in urls:
        # print(each.string)
        if li_nums == url_nums:
            url = each.get("href")
            print("url", url)
        url_nums += 1
        # print("-" * 6)

    # 发布日期
    pub_date = item.select('div')[1].string
    print('pub_date:', pub_date, type(pub_date))
    # 价格
    price = item.select('div')[-1].string
    print('price:', price, type(price))
    print("=" * 20)
    li_nums += 1
