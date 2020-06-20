"""
level 2:
案例：包图网图片爬虫
https://ibaotu.com/sy/

"""

import requests
import re
import redis
import json


def down(url):
    '''
    下载制定url的页面内容
    :param url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    # html = response.content.decode(response.apparent_encoding, 'ignore')
    return html


if __name__ == '__main__':
    try:
        r = redis.StrictRedis(host='localhost', port=6379)
    except Exception as e:
        print(e)
    # 条目
    pat1 = re.compile(r'<li class="pr-container ".*?>(.*?)</li>', re.S | re.M)

    # 为了方便加个title
    pat5 = re.compile(r'<h2.*?class="works-name">(.*?)</h2>', re.S | re.M)

    # 图片（详情页获取）
    # 详情连接
    pat2 = re.compile(r'<a.*?href="(.*?)"', re.S | re.M)
    # 图片地址(他有两种格式和类名变化)
    pat3 = re.compile(r'<div.*?class="stencil-img".*?src="(.*?)"', re.S | re.M)
    # pat3 = re.compile(r'<div.*?class="stencil".*?src="(.*?)"', re.S | re.M)
    pat4 = re.compile(r'<div.*?class="img-wrap ".*?src="(.*?)"', re.S | re.M)

    for page in range(1, 11):
        if page == 1:
            url = 'https://ibaotu.com/sy/'
        else:
            str_page = str(page)
            url = 'https://ibaotu.com/sy/17-0-0-0-0-' + str_page + '.html'
        print('page:', page)
        html = down(url)
        # print(html)
        # 数据提取
        ls = pat1.findall(html)
        print('len:', len(ls))
        for item in ls:
            # print('item:',item)

            # 详情连接
            match_obj = pat2.search(item)

            if match_obj != None:
                # 拼接完整路径
                detail_url = "https:" + match_obj.group(1)
            else:
                detail_url = '空'
            print('detail_url:', detail_url)
            # 获取图片
            # 请求详情页
            detail_html = down(detail_url)
            # print(html)
            # 数据提取
            match_obj = pat3.search(detail_html)
            if match_obj != None:
                # 拼接完整路径
                img_url = "https:" + match_obj.group(1)
            else:
                match_obj = pat4.search(detail_html)
                if match_obj != None:
                    # 拼接完整路径
                    img_url = "https:" + match_obj.group(1)
                else:
                    img_url = '空'
            print('img_url:', img_url)
            # 图片标题
            match_obj = pat5.search(detail_html)

            if match_obj != None:
                title = match_obj.group(1)
            else:
                title = '空'
            print('title:', title)
            print('=' * 200)
            # 存储
            data = {
                'title': title,
                'detail_url': detail_url,
                'img_url': img_url,
            }
            data = json.dumps(data)  # dict===>字符串
            r.lpush('ibaotu', data)
