# level 2:
# 案例：空姐网相册爬虫(bs4)
# http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1
# 爬取相册照片，用uid + picid +'.jpg'命名，保存到images目录下


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

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

url = "http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1"

# 使用之前封装好的讯代理
response = down(url=url)

# html = response.content.decode(response.apparent_encoding)
html = response.text
# print(html)
# 提取数据
soup = BeautifulSoup(html, 'lxml')
ls = soup.select('div.ptw  li ')
print('len:', len(ls))

for item in ls:
    detail_url = item.select_one('a').get('href')
    # 请求章节的详情页面
    print("准备进入详情", detail_url)
    name = re.findall(r'\d+', detail_url)
    print("".join(name))
    detail_name = "".join(name)
    # 进入详情获取页面
    html = down(detail_url).text
    # bs4做解析
    detail_soup = BeautifulSoup(html, 'lxml')
    # 分页列表
    pgs = detail_soup.select('div.pg  a ')
    print("含有分页", pgs)
    # 图片列表
    imgs = detail_soup.select('div.bm_c li > a > img')
    print(imgs, len(imgs))
    print("+" * 20)
    for img in imgs:
        img_url = img.get('src')
        # print(img_url)
        # name = os.path.basename(img_url)
        # 正则匹配
        # name = re.findall(r'\d+', "http://www.kongjie.com/home.php?mod=space&uid=1026522&do=album&picid=864855")
        # print(name)
        # ['1026522', '864855'] 使用join合并为字符串
        name = re.findall(r'\d+', img_url)
        print("".join(name))
        imgname = "".join(name)
        img_response = requests.get(img_url, headers)
        # 一个详情下的uid+id还是有重复的，再加上图片中的数字
        with open('imgs/' + detail_name+imgname+".jpg", "wb")as file:
            file.write(img_response.content)
