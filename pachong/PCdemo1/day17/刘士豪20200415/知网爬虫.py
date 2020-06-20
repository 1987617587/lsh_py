# author:lsh
# datetime:2020/4/15 20:16 
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
import random
import time

import requests

'''
level 2:
案例：爬取知乎网站爬虫
爬取标题和概要信息
'''
url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LYZ28N)',
    'Cookie': '_zap=79a0f994-e821-4805-83e6-4a2333896bce; d_c0="ACDbeCC--BCPTjm1V1ekSb2UhXCIbDicb7I=|1584350745"; _ga=GA1.2.233589575.1584350748; _xsrf=uYWj9cJScc9nDB3IRQcGKqXBFrbOBgcG; _gid=GA1.2.228924450.1586931905; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1586221081,1586756830,1586931904,1586952875; capsion_ticket="2|1:0|10:1586952875|14:capsion_ticket|44:NjVhMzEzNzAwYmM1NDMwYzg2NTYyOWQwYjgyNTA5MTA=|c6b3c4e73a95f772733691256afc659c3eeacaa63c18d29e36d2ff6c3a38b139"; SESSIONID=758cOBsKZrgQXlBBprVLpF932aIu4FVenvASuu1HXe7; JOID=W1wWAUifFt3GyH4eTZQhRJK_8QZWpSTkpI0xagfPab2WkRhRCDnqS5PPdBhNc360oICxZialoCj3FpaCrIkqL8s=; osd=UlwTCkKWFtjNwnceSJ8rTZK6-gxfpSHvroQxbwzFYL2TmhJYCDzhQZrPcRNHen6xq4q4ZiOuqiH3E52IpYkvJME=; z_c0="2|1:0|10:1586952925|4:z_c0|92:Mi4xSGcyWEdnQUFBQUFBSU50NElMNzRFQ1lBQUFCZ0FsVk4zVWlFWHdDYnBhbHJtb0ZlRDVwb2lfdUQwOWQwNnpEZ3NB|9b3607e2cdd3b4820e7c633b903b8d524e15f6c3dd6a9c26e57626ef66693659"; tst=r; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1586953831; KLBRSID=e42bab774ac0012482937540873c03cf|1586953835|1586952874',

}

# session_token: 7eba65d06cbb8a960fc295d56f2e95b0
# desktop: true
# page_number: 5 +=1
# limit: 6
# action: down
# after_id: 23 从0+=6
# ad_interval: -1
max_page = 2
page = 1
while page <= max_page:
    print(f'page:{page}')
    params = {
        'session_token': '7eba65d06cbb8a960fc295d56f2e95b0',
        "desktop": 'true',
        "page_number": page,
        "action": 'down',
        "after_id": (page - 1) * 6 - 1,
        "ad_interval": -1,
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    # print(data)
    ls = data['data']
    print(f'len:{len(ls)}')
    # for item in ls:
    #     try:
    #         title = item['target']['question']['title']
    #         print(f'title:{title}')
    #         content = item['target']['excerpt']
    #         print(f'content:{content}')
    #     except Exception as e:
    #         print(e)
    for item in ls:
        if 'target' in item:
            if 'question' in item['target']:
                if 'title' in item['question']:
                    title = item['target']['question']['title']
                elif 'title' in item['target']:
                    title = item['target']['title']
                else:
                    title = '空'
            elif 'title' in item:
                title = item['title']
            else:
                title = '空'
            if 'excerpt' in  item['target']:
                content = item['target']['excerpt']
            else:
                content = '空'

    time.sleep(random.random())
    is_end = data['paging']['is_end']
    print(is_end, type(is_end))
    if is_end:
        break
    page += 1
