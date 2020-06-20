from lxml import etree

import requests

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
# response = requests.get("https://www.baidu.com/s?wd=%E9%95%BF%E5%9F%8E", headers=headers)
# print('再次查看请求头：', response.request.headers)
# print(response.content.decode('utf8'))
# 带参查询
url = "https://www.baidu.com/s?"
params = {
    "wd": "长城",
    "ie": "utf-8"
}
response = requests.get(url, params=params, headers=headers)
# print(response.content.decode('utf8'))
# 利用lxml把字符串解析成html文档对象
text = response.content.decode('utf8')
html = etree.HTML(text)
print(html)
# 把html文档对象做序列化处理返回
# print(etree.tostring(html).decode())
# 查找根节点
print("查找根节点:", html.xpath('/html'))
print("查找根节点:", html.xpath('//title'))
print("查找根节点:", html.xpath('/html/head'))
print("查找根节点:", html.xpath('/html/head/title'))
print("查找根节点:", html.xpath('/html/head/link'))
