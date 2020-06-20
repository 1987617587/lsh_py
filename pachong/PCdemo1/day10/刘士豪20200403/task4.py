'''

海报图片爬虫
http://www.haibao.com/
http://pic.haibao.com/hotimage/
爬取海报图片
'''
import random

import requests
import json

from lxml import etree
import time
# 一直不能下拉获取数据，无数次实践发现headers注释掉真香
headers = {
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    # 'Cookie': 'hbUnregUserId=71AFB28E-0026-4277-9362-2A55D7A38CE1; __captcha_comment=83X3oWfjlgdrHcOw%2BtFVLURC2YmzTAcNDFRvf3smTHM%3D; Hm_lvt_793a7d1dd685f0ec4bd2b50e47f13a15=1585914997,1585923217; Hm_lvt_9448a813e61ee0a7a19c41713774f842=1585914997,1585923217; Hm_lvt_06ffaa048d29179add59c40fd5ca41f0=1585914997,1585923217; Hm_lpvt_06ffaa048d29179add59c40fd5ca41f0=1585923239; Hm_lpvt_9448a813e61ee0a7a19c41713774f842=1585923239; Hm_lpvt_793a7d1dd685f0ec4bd2b50e47f13a15=1585923239',
    # 'content-type': 'application/json',
    # 'referer': 'http://pic.haibao.com/hotimage/',
    # 'Content-Length': '7',
    # 'Host': 'pic.haibao.com',
    # 'Origin': 'http://pic.haibao.com',
    # 'Pragma': 'no-cache',
    # 'X-Requested-With': 'XMLHttpRequest',
}
# url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp=Fri%20Apr%2003%202020%2019:58:15%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
url = 'http://pic.haibao.com/ajax/image:getHotImageList.json'
# url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp=Fri%20Apr%2003%202020%2022:51:43%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
skip = 0
while skip < 200:
    stamp_time = 'Fri Apr 03 2020 ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' GMT 0800 (中国标准时间)'
    print(stamp_time)
    params = {
        'stamp': stamp_time
    }
    data = {
        'skip': (None,skip),
        # 'stamp': (None,stamp_time)
    }
    #
    # response = requests.post(url, data=json.dumps(data), headers=headers)
    response = requests.post(url, data=data,params=params, headers=headers)
    # print(response.text)
    html = json.loads(response.text)['result']['html']
    hasMore = json.loads(response.text)['result']['hasMore']
    skip = json.loads(response.text)['result']['skip']
    print(f'hasMore:{hasMore}')
    print(f'skip:{skip}')
    # print(html)
    # # 对处理后的html文本进行解析
    html = etree.HTML(html)
    ls = html.xpath('//div[contains(@class,"jsImageContainer")]')
    print(f'len:{len(ls)}')
    for each in ls:
        # 名称
        title = each.xpath('.//div[@class="pagelibox"]//img/@alt')[0]
        print(f'title:{title}')
        # 链接
        img_url = each.xpath('.//div[@class="pagelibox"]//img/@data-original')[0]

        print(f'img_url:{img_url}')
    print("准备向下抓取数据...")
    time.sleep(random.random()+1)
