'''

https://www.lagou.com/zhaopin/Python/?labelWords=label

爬取python职位相关信息：
标题，链接，发布时间，薪资待遇，学历，公司名称，福利待遇，公司说明
爬取10页
数据存储csv格式
'''


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

url = "https://www.lagou.com/zhaopin/Python/?labelWords=label"

# 标题，链接，发布时间，薪资待遇，学历，公司名称，福利待遇，公司说明
# Title, link, release time, salary, education, company name, benefits, company description
try:
    file = codecs.open('lagou.csv', 'w', encoding='utf-8')
    wr = csv.writer(file)
    wr.writerow(['标题', '链接', '发布时间', '薪资待遇', '学历','公司名称', '福利待遇', '公司说明'])
except Exception as e:
    print(e)

i = 0
def get_text(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    html = etree.HTML(html)
    # print(html)
    # 分析结果，编写xpath匹配表达式
    ls = html.xpath('//ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
    print(f'len{len(ls)}')
    for each in ls:
        # title, detail_url, pub_date, salary, education, company_name, benefits, company_description
        title = each.xpath('.//a[@class="position_link"]/h3/text()')[0]
        print(title)
        detail_url = each.xpath('.//a[@class="position_link"]/@href')[0]
        print(detail_url)
        pub_date =  each.xpath('.//span[@class="format-time"]/text()')[0]
        print(pub_date)

        salary = each.xpath('.//div[@class="p_bot"]/div[@class="li_b_l"]/span/text()')[0]
        print(salary)
        education =  each.xpath('.//div[@class="p_bot"]/div[@class="li_b_l"]/text()')[2].strip()
        # //*[@id="s_position_list"]/ul/li[4]/div[1]/div[1]/div[2]/div/text()
        print(education)
        company_name =  each.xpath('.//div[@class="company_name"]/a/text()')[0]
        print(company_name)
        benefits =  each.xpath('//div[@class="industry"]/text()')[0].strip()
        print(benefits)
        company_description =  each.xpath('.//div[@class="li_b_r"]/text()')[0]
        print(company_description)

        time.sleep(random.random())
        # 数据存储
        wr.writerow([title, detail_url, pub_date, salary, education, company_name, benefits, company_description])
        # 翻页
    global i
    print(i,"++++++++")

    i+=1
    if i<= 10:
        print(i, "++++++++")

        get_text('https://www.lagou.com/zhaopin/Python/'+str(i)+'/?filterOption=2&sid=d9649914c86649fbb098f16db6024851')
        get_text('https://www.lagou.com/zhaopin/Python/'+str(i))




if __name__ == '__main__':
    get_text(url)
    # file.close()

