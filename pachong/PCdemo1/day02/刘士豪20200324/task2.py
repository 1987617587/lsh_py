# level 2:
# 案例：链家二手房
# https://sh.lianjia.com/ershoufang/
# 提取标题，链接，单价，总价，基本信息，房源特色信息
# 保存到mysql数据库

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
# 带参查询
# https://sh.lianjia.com/ershoufang/pg2/
url = "https://sh.lianjia.com/ershoufang/"
start_pg = input("请输入开始页数：")
end_pg = input("请输入截至页数：")
try:
    # 根据浏览器反馈操作
    for i in range(int(start_pg), int(end_pg) + 1):
        if i >= 2:
            params = {
                "pg": i
            }
        else:
            params = None
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        # 使用之前封装好的讯代理
        # html = down(url=url)
        html = response.content.decode(response.apparent_encoding)
        print(html)
        # 提取数据
        html = etree.HTML(html)
        print(html)

        print("+++")
        # 分析结果，编写xpath匹配表达式
        ls = html.xpath('//div[@class="info clear"]')

        print('len', len(ls))

        for item in ls:
            # 标题
            # title = item.xpath('.//a[@class="j_th_tit "]/text()')[0]
            title = item.xpath('.//a/text()')[0]
            print('title', title)
            # 详情链接
            detail_url = item.xpath('.//a/@href')[0].strip()
            print('detail_url', detail_url)
            # 进入详情
            response = requests.get(detail_url, headers=headers)
            print("进入详情链接", response.url)
            html = response.content.decode(response.apparent_encoding)
            print(html)
            # 提取数据
            html = etree.HTML(html)
            # print(html)
            print("#" * 10, "总价")
            unit_price = html.xpath('//div[@class="price "]//span/text()')[0]
            unit = html.xpath('//div[@class="price "]/span[@class="unit"]/span/text()')[0]
            print(unit_price, unit)

            print("#" * 10, "单价")
            price = html.xpath('//span[@class="unitPriceValue"]/text()')[0]
            i = html.xpath('//span[@class="unitPriceValue"]/i/text()')[0]
            print(price, i)
            with open("链家.txt", 'a', encoding='utf-8') as file:
                file.write(title + "\t" + detail_url + "\t" + unit_price + unit + "\t" + price + i + "\t")

            print("#" * 10, "基本信息--基本属性")
            # 分析结果，编写xpath匹配表达式
            #     class="introContent" li 下<span class="label">房屋户型</span>
            arr = html.xpath('//div[@class="introContent"]//li')
            print(len(arr))

            for intro in arr:
                info_label = intro.xpath('.//span[@class="label"]/text()')[0]

                info = intro.xpath('./text()')[0]
                print("+" * 30, info_label, info)
                # 数据存储
                with open("链家.txt", 'a', encoding='utf-8') as file:
                    file.write(info + "\t")
            print("#" * 10, "基本信息--交易属性")
            # 分析结果，编写xpath匹配表达式
            #     class="introContent" li 下<span class="label">房屋户型</span>
            arr = html.xpath('//div[@class="transaction"]//li')
            print(len(arr))

            for intro in arr:
                info_label = intro.xpath('.//span[@class="label"]/text()')[0]
                info = intro.xpath('.//span[last()]/text()')[0]
                print("+" * 30, info_label, info)
                # 数据存储
                # 数据存储
                with open("链家.txt", 'a', encoding='utf-8') as file:
                    file.write(info + "\t")

            print("#" * 10, "房源特色")
            # 分析结果，编写xpath匹配表达式
            #     class="baseattribute clear" 下div[@class="content"]
            arr = html.xpath('//div[@class="baseattribute clear"]//div[@class="content"]/text()')
            print(len(arr))

            for info in arr:
                print("+" * 30, info)
                # 数据存储
                with open("链家.txt", 'a', encoding='utf-8') as file:
                    file.write(info + "\t")
            with open("链家.txt", 'a', encoding='utf-8') as file:
                file.write("\n")
        # 设置随机的延迟时间
        time.sleep(random.random())
except:
    print("未找到相应数据")
