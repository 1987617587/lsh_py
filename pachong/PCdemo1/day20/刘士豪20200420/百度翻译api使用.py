# author:lsh
# datetime:2020/4/20 17:46 
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
# 模块导入
import execjs

import requests


def translate(content):
    headers = {
        'Cookie': 'PSTM=1583895540; BIDUPSID=C92D780B805E9621887192AB4135A9D5; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=15F6AA3C5B2E63BA787D2BD038F1BBBD:SL=0:NR=10:FG=1; MCITY=-%3A; H_WISE_SIDS=140842_142081_143803_142062_142112_141910_143390_143856_143879_141747_142512_139171_141900_142780_136862_131246_142909_141261_138165_138883_140259_141942_127969_142872_140065_143998_140593_143059_143492_131953_140351_143468_143922_143275_131423_144003_107315_138595_143959_143477_142911_142273_110085; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22pt%22%2C%22text%22%3A%22%u8461%u8404%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDUSS=t-c0RHek9KeURmakhrSUcxbU5pM0xtUmo4OX4tZ0xMUmZpcTBiMWxTTkdqcnRlRVFBQUFBJCQAAAAAAAAAAAEAAABJhg6pusC45zE5ODc2MTc1ODcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEYBlF5GAZReM0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587381012,1587381421,1587382401,1587391542; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587391542; __yjsv5_shitong=1.0_7_4525be5c29f1971dbd56b09468ba79a2389d_300_1587391543614_42.231.63.159_52aec175; yjs_js_security_passport=f520d7789d6d430f418ef65665b4f874f053c8b6_1587391544_js',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    }
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

    with open('baidu.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    sign = ctx.call('e', content)

    print(sign)
    data = {
        'from': 'en',
        'to': 'zh',
        'query': content,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': 'c2be4f3f6e5acee2788919dbe05b4c9b',
        'domain': 'common',
    }
    response = requests.post(url, data=data, headers=headers)
    # print(response.text)
    target = response.json()['trans_result']['data'][0]['dst']
    return target


if __name__ == '__main__':
    while True:
        content = input("请输入单词:")
        print(translate(content))
