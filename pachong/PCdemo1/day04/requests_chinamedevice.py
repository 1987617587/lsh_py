# level
# 1:
# 案例：医疗器械网爬虫(bs4):
# http://www.chinamedevice.cn/
# 爬取大的分类
# 爬取产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，
# 生产企业，联系人，联系电话，移动电话，手机，单位地址
# 数据保存到mongodb中
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
        collec = db['yiliaoqixie']
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


# 获取器械分类列表
def parse_catetory_list(url):
    currcent_url, soup = requests_url(url)

    ls = soup.select('a.f12')
    print(f'catetory len:{len(ls)}')
    for each in ls:
        category_url = each.get('href')
        # 拼全路径进入下一步操作
        url = "http://www.chinamedevice.cn/" + category_url
        parse_product_list(url)
        # 分类


def parse_product_list(url):
    print(f"category_url:{url}")
    currcent_url, soup = requests_url(url)

    ls = soup.select('div.list > ul > li > h3 > span > a')
    print(f'product_list len:{len(ls)}')
    if len(ls) > 0:
        for each in ls:
            product_url = each['href']
            parse_product_detail(product_url)
            # 稍稍等待
            time.sleep(random.random())

    # 翻页
    next_page_btn_ls = soup.select('a.fno')
    print("next_page_btn_ls", next_page_btn_ls)
    if len(next_page_btn_ls) > 0:
        next_page = next_page_btn_ls[-1]
        # 最后一个按钮可能不是下一页按钮，加个文本判断
        if next_page.get_text() == '下一页':
            next_page_url = next_page['href']
            # 先申明要替换的部分
            pat = re.compile(r'(\d+\.html)')
            # 用正则表达式做替换,currcent_url待（匹配）替换的字符串，next_page_url替换的字符串
            next_page_url = pat.sub(next_page_url, currcent_url)
            print('next_page_url:', next_page_url)
            # 递归调用,开始爬取下一页
            if next_page_url:
                parse_product_list(next_page_url)


# 产品详情
def parse_product_detail(url):
    print(f"photo_detail_url:{url}")
    currcent_url, soup = requests_url(url)

    product_name = soup.select_one('div#main h1').get_text()
    print(f'产品名:{product_name}')
    product_img_url = soup.select_one('div.img > a > img').get('src')
    print(f'产品图片链接:{product_img_url}')
    product_li_ls = soup.select('div.text01 > ul > li')
    # 产品类别   第2个li下面有两个元素，拿第二个
    cate_name = product_li_ls[1].contents[1].string.strip()
    print("产品类别", cate_name)

    # 批准文号
    approval_number = product_li_ls[3].select_one('h3').get_text()
    print("批准文号", approval_number)

    # 产品规格
    spec = product_li_ls[4].contents[1].string.strip()
    print("产品规格", spec)
    # 产品说明
    descropition = soup.select_one('dd.text03').get_text().strip()
    print('产品说明', descropition)
    # print(f'product_list len:{len(ls)}')

    # 生产企业
    pub_factory = soup.select_one('li.bgwhite.pt > h3 > a').get_text().strip()
    print("生产企业", pub_factory)

    # 联系人

    contactor = soup.select('dd.text04 > ul > li')[2].get_text().strip()
    contactor = contactor.split('：')[-1]
    print("联系人", contactor)
    # 联系电话
    descropition_tel = soup.select('dd.text04 > ul > li')[3].contents[0].string.strip()
    descropition_tel = descropition_tel.split('：')[-1]

    print('联系电话', descropition_tel)
    # 地址
    address = soup.select('dd.text04 > ul > li')[9].get_text().strip()
    address = address.split('：')[-1]

    print('地址', address)
    print('*' * 20)
    # print(f'product_list len:{len(ls)}')
    # 存储
    data = {
        'product_name': product_name,
        'product_img_url': product_img_url,
        'cate_name': cate_name,
        'approval_number': approval_number,
        'spec': spec,
        'descropition': descropition,
        'pub_factory': pub_factory,
        'contactor': contactor,
        'descropition_tel': descropition_tel,
        'address': address,

    }
    collec.insert(data)


if __name__ == '__main__':
    collec = get_collection()
    parse_catetory_list("http://www.chinamedevice.cn/")
