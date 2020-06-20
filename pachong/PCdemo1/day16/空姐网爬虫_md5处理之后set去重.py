# level 2:
# 案例：空姐网相册爬虫(bs4)
# http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1
# 爬取相册照片，用uid + picid +'.jpg'命名，保存到images目录下


# 页面请求
import os
import re
from hashlib import md5

import pymongo
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


def init():
    set1 = set()
    return set1


# 通过函数展示注意操作步骤
# 设定UA
def get_ua():
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    return headers


# 获取空姐网相册列表
def parse_album_list(url):
    response = requests.get(url, headers=get_ua())
    # response = down(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取相册列表（ul有多个class 使用.ml.mla.cl表示）
    ls = soup.select('ul.ml.mla.cl > li > div > a')
    print(f'album len:{len(ls)}')
    for each in ls:
        # album_url = each['href']
        # album_url = each.attrs['href']
        album_url = each.get('href')
        # 进入下一步操作
        parse_photo_list(album_url)
    # 翻页 有翻页按钮就拿过来（没有的话选择器选择不到）
    next_page_btn_ls = soup.select('a.nxt')
    if len(next_page_btn_ls) > 0:
        next_page_url = next_page_btn_ls[0].get('href')
        print('next_page_url:', next_page_url)
        # 递归调用,开始爬取下一页
        parse_album_list(next_page_url)


# 获取空姐网相册下的图片列表
def parse_photo_list(url):
    print(f"album_url:{url}")
    response = requests.get(url, headers=get_ua())
    # response = down(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取当前相册中的图片列表
    ls = soup.select('ul.ptw.ml.mlp.cl > li > a')
    print(f'photo list len:{len(ls)}')
    if len(ls) > 0:
        for each in ls:
            photo_url = each.attrs['href']
            parse_photo_detail(photo_url)
            # 稍稍等待
            time.sleep(random.random())
    # 翻页
    next_page_btn_ls = soup.select('a.nxt')
    if len(next_page_btn_ls) > 0:
        next_page_url = next_page_btn_ls[0].get('href')
        print('next_page_url:', next_page_url)
        # 递归调用,开始爬取下一页
        parse_photo_list(next_page_url)


# 获取空姐网具体图片
def parse_photo_detail(url):

    # print(f"photo_detail_url:{url}")
    hash_url= md5(url.encode('utf-8'))
    url_pwd = hash_url.hexdigest()

    if url_pwd in photo_set:
        print("该页面已经爬取过")
    else:
        # 正则匹配
        pat = re.compile(r'uid=(\d+).*?picid=(\d+)')
        match_obj = pat.search(url)
        if match_obj != None:
            uid = match_obj.group(1)
            picid = match_obj.group(2)
            print(uid, picid)
            print(f"photo_detail_url:{url}")
            response = requests.get(url, headers=get_ua())
            soup = BeautifulSoup(response.text, 'lxml')
            img_url = soup.select_one('img#pic')['src']
            down_photo(img_url, uid, picid)
            # 添加url到set集合
            photo_set.add(url_pwd)


# 图片下载
def down_photo(img_url, uid, picid):
    print(img_url, uid, picid)
    print('=' * 9)
    img_response = requests.get(img_url, get_ua())
    # 一个详情下的uid+id还是有重复的，再加上图片中的数字
    with open('images/' + str(uid + picid) + ".jpg", "wb")as file:
        # 字节流
        file.write(img_response.content)


if __name__ == '__main__':
    photo_set = init()
    parse_album_list("http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1")
