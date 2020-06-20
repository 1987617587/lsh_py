# level
# 1:
# 案例：医疗器械网爬虫(bs4):
# http://www.chinamedevice.cn/
# 爬取大的分类
# 爬取产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，
# 生产企业，联系人，联系电话，移动电话，手机，单位地址
# 数据保存到mongodb中

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


# 获取器械分类列表
def parse_album_list(url):
    response = requests.get(url, headers=get_ua())
    # response = down(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取相册列表（ul有多个class 使用.ml.mla.cl表示）
    ls = soup.select('div.nr_4 div.type > ul > li > a')
    # ls = soup.find_all('div.nr_4 div.type > ul > li > a')
    print(f'album len:{len(ls)}')
    for each in ls:
        # album_url = each['href']
        # album_url = each.attrs['href']
        album_url = each.get('href')
        # 抛弃英文分类
        if "html" in album_url:
            print("+" * 30)
            # 拼全路径进入下一步操作
            url = "http://www.chinamedevice.cn/" + album_url
            parse_photo_list(url)
            # 分类


def parse_photo_list(url):
    print(f"album_url:{url}")

    response = requests.get(url, headers=get_ua())
    # response = down(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # 产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，
    # TODO

    ls = soup.select('div#main div.sc-list > h4 ')
    print(f'photo list len:{len(ls)}')
    if len(ls) > 0:
        for each in ls:
            photo_url = each.select_one('a')['href']
            # photo_url = each.attrs['href']
            parse_photo_detail("http://www.chinamedevice.cn/product/" + photo_url)

            # 稍稍等待
            time.sleep(random.random())


# 公司列表有分页
def parse_photo_detail(url):
    print(f"photo_detail_url:{url}")
    response = requests.get(url, headers=get_ua())
    soup = BeautifulSoup(response.text, 'lxml')
    ls = soup.select('div.gys dd > table')
    print(f'blank list len:{len(ls)}')
    for blank in ls:
        #  生产企业，联系人，联系电话，移动电话，手机，单位地址
        blank_name = blank.select_one('a.green.f14.u').string
        print("blank_name:", blank_name)
        # 下面的不会获取 TODO
        # 电话
        blank_tel = blank.select('tr td')[4].string
        print("blank_tel:", blank_tel)
        # 传真
        blank_send = blank.select('tr td')[6].string
        print("blank_send:", blank_send)
        # 地址
        blank_address = blank.select('tr td')[8].string
        print("blank_address:", blank_address)
        # 产品名 和 url可以存储
        name = soup.select('b.orange.f14')[0].string
        print("产品名：", name, type(name), type(str(name)))
        collec.insert({'name': str(name), 'url': url, 'blank_name': str(blank_name), 'blank_tel': str(blank_tel),
                       'blank_send': str(blank_send), 'blank_address': str(blank_address), })

    # # 翻页
    next_page_btn_ls = soup.select('h6 div a')
    print("next_page_btn_ls", next_page_btn_ls)
    if len(next_page_btn_ls) > 0:
        next_page_url = next_page_btn_ls[-1].get('href')
        print('next_page_url:', next_page_url)
        # 递归调用,开始爬取下一页
        if next_page_url:
            parse_photo_list("http://www.chinamedevice.cn/" + next_page_url)


if __name__ == '__main__':
    parse_album_list("http://www.chinamedevice.cn/")
