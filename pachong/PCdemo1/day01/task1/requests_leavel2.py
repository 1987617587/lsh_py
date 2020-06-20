# level 1:
# 1、阅读课件
# 2、 什么是 http 协议？
# 3、 http 和 https 的区别？
# 4、 常见的状态码有哪些？
# 5、什么是爬虫？爬虫有哪些分类？
# 6、 数据爬取的步骤有哪些？
# 7、案例：百度模拟搜索“长城”
# 8、阅读课件，掌握xpath的用法

# level 2:
# 爬取https://www.qq.com/
# 保存页面为，qq.html
#
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
url = 'https://www.qq.com/'
response = requests.get(url, headers=headers)
print(response.content)
# 存储数据
with open('qq.html', 'wb') as file:
    file.write(response.content)

# 爬取搜狗动漫
# http://kan.sogou.com/dongman/
# 保存页面为，dongman.html
#

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
url = 'http://kan.sogou.com/dongman/'
response = requests.get(url, headers=headers)
print(response.content)
# 存储数据
with open('dongman.html', 'wb') as file:
    file.write(response.content)
# 搜狐健康
# http://health.sohu.com/?spm=smpc.home.top-nav.24.1550453761461Q0shOpW
# 保存页面为，sohuhealth.html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
url = 'http://health.sohu.com/?spm=smpc.home.top-nav.24.1550453761461Q0shOpW'
response = requests.get(url, headers=headers)
print(response.content)
# 存储数据
with open('sohuhealth.html', 'wb') as file:
    file.write(response.content)
