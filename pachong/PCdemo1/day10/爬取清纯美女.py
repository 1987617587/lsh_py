import re

import pymysql
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='girl')
cur = conn.cursor()
url = 'http://www.jinvjie.com/m-list-116.html'

response = requests.get(url, headers=headers)
html = response.text
# print(html)
pat1 = re.compile(r'(<a.*?class="Pli-litpic".*?</a>)', re.S | re.M)
pat2 = re.compile(r'<img.*?src="(.*?)"', re.S | re.M)

# 数据提取
ls = pat1.findall(html)
print('len:', len(ls))
for img in ls:
    # print(img)
    img_url = pat2.findall(img)[0]
    print(img_url)
    strsql = 'insert into qingchun values(0,%s)'
    params = [img_url]
    cur.execute(strsql, params)
    conn.commit()

# 翻页按钮
# class="pagination"/li[-1]
html = etree.HTML(html)

next_page = html.xpath('//ul[@class="pagination"]/li[6]/a/@href')[0]
next_url = 'http://www.jinvjie.com'+next_page

print(next_url)