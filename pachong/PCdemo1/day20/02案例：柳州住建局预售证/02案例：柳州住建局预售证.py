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
import json
import random
import time

url = 'http://zjj.zhuzhou.gov.cn/fcjadpater/select/WWW_YSXK_002'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

for page in range(1, 5):
    print('page:', page)
    data = {
        'verifycode': '',
        'cdno': '',
        'lname': '',
        'pageIndex': '2',
        'pageSize': '15',
    }
    response = requests.post(url,data=data,headers=headers)
    data = response.json()['rows']
    data = json.loads(data)
    print(type(data))

    PIC_SERVER_PREFIX = "http://218.75.204.3:5636/"
    for item in data:
        print(item)
        bid = item['bid']
        print('bid:',bid)
        cdno = item['cdno']
        print('cdno:',cdno)
        fpath = item['fpath']
        print('fpath:',fpath)
        pid = item['pid']
        print('pid:',pid)
        pname = item['pname']
        print('pname:',pname)
        print('='*200)
        img_url = PIC_SERVER_PREFIX + fpath
        img = requests.get(img_url,headers=headers).content
        img_path = './images/'+cdno +'.jpg'
        with open(img_path,'wb') as file:
            file.write(img)
        time.sleep(random.random())

