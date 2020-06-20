# author:lsh
# datetime:2020/4/20 14:27 
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
import hashlib
import random
import time

import requests


def translate(content):
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1134804966@10.108.160.102; OUTFOX_SEARCH_USER_ID_NCOO=1658766101.3843126; JSESSIONID=aaaXrB6kkgXov-bVZlwgx; ___rl__test__cookies=1587363838492',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    }
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    ctime = int(time.time() * 1000)
    salt = str(ctime) + str(random.randint(1, 10))
    client = 'fanyideskweb'
    key = 'Nw(nmmbP%A-r6U3EUn]Aj'
    sign = hashlib.md5((client + content + salt + key).encode('utf-8')).hexdigest()
    print(sign)
    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': client,
        'salt': salt,
        'sign': sign,
        'ts': ctime,
        'bv': '7bcd9ea3ff9b319782c2a557acee9179',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    response = requests.post(url,data=data,headers=headers)
    target = response.json()

    print(target)
    result = target['translateResult'][0][0]['tgt']
    print(result)



if __name__ == '__main__':
    while True:
        content = input("请输入单词:")
        translate(content)

