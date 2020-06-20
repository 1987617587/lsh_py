#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

from selenium import webdriver
from lxml import etree
import re

url = 'https://g.hongshu.com/content/93416/13901181.html'
browser = webdriver.Chrome()
browser.get(url)
words = browser.execute_script('return words;')
print(words,type(words))
html = browser.page_source
pat1 = re.compile(r'(<span class="context_kw\d+">.*?</span>)')
pat2 = re.compile(r'class="context_kw(\d+)"')
def func(m):
    s = m.group(1)
    index = int(pat2.search(s).group(1))
    return words[index]

html = pat1.sub(func,html)
html = etree.HTML(html)
ls = html.xpath('//div[@class="rdtext"]/p//text()')
content = '\n'.join(ls)
print(content)
browser.close()


