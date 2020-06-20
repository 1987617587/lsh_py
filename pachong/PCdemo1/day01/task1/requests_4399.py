"""
http://www.4399.com/?haoqqdh
爬取手游，专辑，儿童，动作，射击，益智，休闲，体育，冒险，女生，合辑，H5游戏，网页游戏，最好玩游戏类表、4399精选游戏、H5游戏精选
的游戏名称和url
保存为4399.txt文件
"""
import requests
from lxml import etree

# 最基本的反反爬
# 设置请求头User_Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
url = 'http://www.4399.com/'
response = requests.get(url, headers=headers)
html = response.content.decode(response.apparent_encoding)
# print(html)
# 提取数据
html = etree.HTML(html)



print("手游")
# 分析结果，编写xpath匹配表达式
# //ul[@class='mi_ul']/span/a
ls = html.xpath("//ul[@class='mi_ul']/li/a")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)
    detail_url = item.xpath('./@href')[0]
    print('detail_url', detail_url)

print("专辑，儿童，动作，射击，益智，休闲，体育，冒险")
# 分析结果，编写xpath匹配表达式
# //div[@class='mi_d']/span/a
ls = html.xpath("//div[@class='mi_d']/span/a")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)
    detail_url = item.xpath('./@href')[0]
    print('detail_url', detail_url)

print("最好玩游戏类表、4399精选游戏、H5游戏精选")
# 分析结果，编写xpath匹配表达式
# //div[@class='mi_g']/sapn/a
ls = html.xpath("//div[@class='mi_g']/sapn/a")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)
    detail_url = item.xpath('./@href')[0]
    print('detail_url', detail_url)

# 分析结果，编写xpath匹配表达式
# //div[@class='mid']
print("网页游戏")
ls = html.xpath("//div[@class='mi_web']/sapn/a")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)
    detail_url = item.xpath('./@href')[0]
    print('detail_url', detail_url)

# 分析结果，编写xpath匹配表达式
# //div[@class='mid']
print("女生，合辑，H5游戏")
ls = html.xpath("//ul[@class='tm_list']/li/a")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)
    detail_url = item.xpath('./@href')[0]
    print('detail_url', detail_url)
