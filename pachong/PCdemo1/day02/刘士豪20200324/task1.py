# 案例：贴吧爬虫
# https://tieba.baidu.com
# 需求：制作爬虫爬取指定贴吧一定页码范围的的信息
# 输入：起始页码，结束页码，贴吧名称
# 提取帖子回复量，标题，链接，作者，保存到tieba.csv文件

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

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}
# 带参查询
# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=300
url = "https://tieba.baidu.com/f?"
bar_name = input("请输入要搜索的贴吧内容：")
start_pn = input("请输入开始页数：")
end_pn = input("请输入截至页数：")
try:
    # 根据浏览器反馈操作
    for i in range(int(start_pn), int(end_pn) + 1):
        params = {
            "kw": bar_name,
            "ie": "utf-8",
            "pn": (i - 1) * 50
        }
        response = requests.get(url, params=params, headers=headers)
        html = response.text
        # print(html)
        # 提取数据
        html = etree.HTML(html)
        print(html)

        print("+++")
        # 分析结果，编写xpath匹配表达式
        # //ul[@class='mi_ul']/span/a

        ls = html.xpath('//li[contains(@class ,"j_thread_list clearfix")]')
        # ls = html.xpath("//div[@class='t_con cleafix']")

        print('len', len(ls))
        # 把路径拼写完成
        base_url = 'https://tieba.baidu.com'
        for item in ls:
            # 标题
            # title = item.xpath('.//a[@class="j_th_tit "]/text()')[0]
            title = html.xpath("//a[@class='j_th_tit ']/text()")[0]
            print('title', title)
            # 详情链接
            detail_url = base_url + item.xpath('.//a[@class="j_th_tit "]/@href')[0].strip()
            print('detail_url', detail_url)
            #  作者
            author = item.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0].strip()
            print('author', author)
            # 回复数
            nums = item.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0].strip()
            print('nums', nums)
            print('=' * 20)

            # 数据存储
            # .csv格式codecs. 在打开文件时避免空行，用open会有空行
            with codecs.open("贴吧" + bar_name + '.csv', 'a', encoding='utf-8') as file:
                wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
                wr.writerow([title, detail_url, author, nums])
        # 设置随机的延迟时间
        time.sleep(random.random())
except:
    print("未找到相应数据")
