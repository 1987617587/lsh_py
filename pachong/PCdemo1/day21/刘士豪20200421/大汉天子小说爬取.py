# author:lsh
# datetime:2020/4/21 20:49 
"""
                                 .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
"""
from selenium import webdriver
from lxml import etree
import hashlib
import random
import time
import re
# 模块导入
import execjs

import requests


url = 'https://g.hongshu.com/content/93416/13901181'

brower = webdriver.Chrome()
brower.get(url)

words = brower.execute_script('return words;')
print(words, type(words))
html = brower.page_source
# <span class="context_kw2"></span>
pat1 = re.compile(r'(<span class="context_kw\d+">.*?</span>)')

pat2 = re.compile(r'class="context_kw(\d+)"')


def func(m):
    s = m.group(1)
    print(s)
    index = int(pat2.search(s).group(1))
    print(index)
    print(words[index])
    return words[index]


html = pat1.sub(func, html)
html = etree.HTML(html)
ls = html.xpath('//div[@class="rdtext"]/p//text()')
content = '\n'.join(ls)
print(content)
brower.close()
