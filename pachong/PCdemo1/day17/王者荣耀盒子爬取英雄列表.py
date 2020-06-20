# author:lsh
# datetime:2020/4/15 16:28 
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

import os
import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作



headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
}
base_url = 'http://gamehelper.gm825.com'
url ='/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=12A84CF38D43ACBCB630B0F61EA6C6B7&ovr=5.1.1&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=Q%2Ft3pkcmtbETmZ7I%2BI%2FHpA%3D%3D&info_ms=Q%2F3EH69Etqj3fT9W9HrrMw%3D%3D&info_ma=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&mno=0&info_la=qma3PGAUEipKo9jsdzK7fA%3D%3D&info_ci=qma3PGAUEipKo9jsdzK7fA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=XhmjJQaGbgGmK3n5sKqZBE5bcWNlcR9GOqaftQYDT%2FE%3D&os_level=22&os_id=80fa5b720bca1407&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=b720bca140780fa5 HTTP/1.1'
# params = {
#     'reqType': '5',
#     'categoryId': '8',
#     'start': page * 12,
# }


# response = requests.get(url, params=params, headers=headers)
response = requests.get(base_url+url,  headers=headers)
# html = response.text
# print(html)
# json格式
data = response.json()
ls = data['list']
# print(ls)
for hero in ls:
    hero_id = hero['hero_id']
    hero_name = hero['name']
    hero_cover = hero['cover']
    print(f'hero_id:{hero_id}')
    print(f'hero_name:{hero_name}')
    print(f'hero_cover:{hero_cover}')
    print('='*100)


time.sleep(random.random())


