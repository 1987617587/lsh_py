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
import time
import random
import hashlib


def translate(content):
    '''
    利用有道翻译API实现翻译功能
    :param content:
    :return:
    '''
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    ctime = int(time.time() * 1000)
    salt = str(ctime) + str(random.randint(1, 10))
    client = "fanyideskweb"
    key = "Nw(nmmbP%A-r6U3EUn]Aj"
    sign = hashlib.md5((client + content + salt + key).encode('utf-8')).hexdigest()
    print('sign:', sign)

    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ctime,
        'bv': '70244e0061db49a9ee62d341c5fed82a',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com/',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=484463584.8730025; OUTFOX_SEARCH_USER_ID=1241098497@10.168.11.144; P_INFO=thompsonkwok; _ntes_nnid=bdb421e91d94536323866818f8c43d2c,1581578089717; _ga=GA1.2.922912839.1585045434; JSESSIONID=aaaAYt8dL7fjr7Bo2lwgx; ___rl__test__cookies=1587362844422',
    }
    response = requests.post(url,data=data,headers=headers)
    target = response.json()
    #print(target)
    result=target['translateResult'][0][0]['tgt']
    return result


if __name__ == '__main__':
    while True:
        content = input('请输入要翻译的单词:')
        result = translate(content)
        print(result)
