# 页面请求
import requests
# 数据提取
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

url = "https://www.52bqg.com/book_86212/"

# 使用之前封装好的讯代理
response = down(url=url)

html = response.content.decode(response.apparent_encoding)
# print(html)
# 提取数据
html = etree.HTML(html)
# print(html)
# 分析结果，编写xpath匹配表达式
ls = html.xpath('//div[@class="box_con"]//dl/dd/a')[4:]

print('len', len(ls))
#
for item in ls:
    # 标题
    title = item.xpath('./text()')
    print('title', title)
    # 详情链接
    detail_url = item.xpath('./@href')[0].strip()
    print('detail_url', detail_url)
    # 进入详情
    # 注意把链接拼接完整
    detail_url = url + detail_url
    detail_response = requests.get(detail_url, headers=headers)
    print("进入详情链接", detail_response.url)
    detail_html = detail_response.content.decode(detail_response.apparent_encoding, "ignore")
    # print(detail_html)
    # 提取数据
    detail_html = etree.HTML(detail_html)

    detail_ls = detail_html.xpath('//div[@id = "content"]/text()')

    # print('len', len(detail_ls))
    print(detail_ls,type(detail_ls))

    # 列表 ===> 字符串
    detail_ls = ''.join(detail_ls)
    print(detail_ls,type(detail_ls))

    print("=" * 8)
    with open("元尊/" + str(title[0]) + ".txt", 'w', encoding='utf-8') as file:
        file.write(detail_ls)
