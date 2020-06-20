import requests
from lxml import etree
import json
import time
import random
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}


def parse(html):
    '''
    提取数据
    :return:
    '''
    html = etree.HTML(html)
    ls = html.xpath('//div[@class="pagelibox"]//img/@data-original')
    count = len(ls)
    print('count:', count)
    for img_url in ls:
        image = requests.get(img_url, headers=headers).content
        image_name = img_url.split('/')[-1]
        image_name = './images/' + image_name
        print(image_name)
        with open(image_name, 'wb') as file:
            file.write(image)
        time.sleep(random.random())


# 1、提取页面中包含的图片
url = 'http://pic.haibao.com/hotimage/'
response = requests.get(url, headers=headers)
html = response.text
count = 0
parse(html)

# 2、异步请求，下载图片
skip = 73
skip = count
url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp='
# stamp: Tue Apr 07 2020 09:27:34 GMT 0800 (中国标准时间)
page = 1
while True:
    GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT 0800'
    stamp = datetime.datetime.now().strftime(GMT_FORMAT)
    stamp = stamp + ' (中国标准时间)'
    print(stamp)
    new_url = url + stamp
    print('new_url:', new_url)
    data = {
        'skip': skip,
    }
    print('page:', page)
    html = requests.post(new_url, data=data, headers=headers).text
    # print(html)
    data = json.loads(html)
    skip = data['result']['skip']
    html = data['result']['html']
    hasMore = data['result']['hasMore']
    print('hasMore:', hasMore, 'skip:', skip)
    print(hasMore == 1)
    parse(html)
    if hasMore == 1:
        time.sleep(random.random())
    else:
        break
