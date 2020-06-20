# author:lsh
# datetime:2020/4/29 17:19 
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
import base64
import json
import zlib

'''
level 2:
案例：小说爬虫
破解小说内容
http://t.shuqi.com/route.php?#!/bid/6813921/cid/678442/ct/read
'''

import requests
from lxml import etree

# 'https://c13.shuqireader.com/webapi/chapter/contentfree/?bookId=6813921&chapterId=678442&ut=1472714702&num=1&ver=1&aut=1587044071&sign=618be62a3defc2b8e4b0ae64fb7bbb55&imei=44953d7ba9812b22354af1f9a9feab8d_shuqi_touch&sn=44953d7ba9812b22354af1f9a9feab8d_shuqi_touch&_=1588151784177'
url = 'http://t.shuqi.com/route.php?#!/bid/6813921/cid/678442/ct/read'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    # 'Cookie': 'JSESSIONID=013b6ef61fd07f84c2c3d4e359aa; JSESSIONID=013b50cca9fa7a624e780b28d396; insert_cookie=71170129; JSESSIONID=013b6ef61fd07f84c2c3d4e359aa'
}
params = {
    'bookId': '6813921',
    'chapterId': '678442',
    'ut': '1472714702',
    'num': 1,
    'ver': 1,
    'aut': 1587044071,
    'sign': '618be62a3defc2b8e4b0ae64fb7bbb55',
    'imei': '44953d7ba9812b22354af1f9a9feab8d_shuqi_touch',
    'sn': '44953d7ba9812b22354af1f9a9feab8d_shuqi_touch',
    '_': '1588151784177',
}
response = requests.get(url, headers=headers)
print(response.text)
# ChapterContent = json.loads(response.text)['ChapterContent']
# print(ChapterContent)
#
#
# token_dict = '“嘶！好痛啊，骨头都要散架了！”'
# # 编码
# encode = str(token_dict).encode()
# # 二进制压缩
# compress = zlib.compress(encode)
# print(compress)
# # base64编码
# b_encode = base64.b64encode(compress)
# print(b_encode)
# # 转成字符串
# token = str(b_encode, encoding='utf-8')
# print(token)