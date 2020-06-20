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

import requests
import execjs
import re
import os
import json

filename = './myjs.js'
with open(filename,'r',encoding='utf-8') as file:
    strjs = file.read()
ctx = execjs.compile(strjs)

url = 'http://ac.scmor.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
response = requests.get(url,headers=headers)
html =response.content.decode(response.apparent_encoding)
pat1 = re.compile(r'var autourl=(\[".*?"\])',re.M|re.S)
match_obj = pat1.search(html)
if match_obj != None:
    str_urls = match_obj.group(1)
    ls = json.loads(str_urls)
    print('len:',len(ls))
    print(ls)
    for item in ls:
        href = ctx.call('strdecode',item)
        print('href:',href,'item:',item)
else:
    print('error...')

