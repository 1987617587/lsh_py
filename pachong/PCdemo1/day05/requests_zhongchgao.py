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
    return html


if __name__ == '__main__':
    try:
        r = redis.StrictRedis(host='localhost', port=6379)
    except Exception as e:
        print(e)
    # 新闻条目
    pat1 = re.compile(r'<div.*?class="news_item".*?(<h3>.*?<a.*?class="comment">.*?</a>).*?<div.*?class="share"',
                      re.S | re.M)
    # 新闻标题
    pat2 = re.compile(r'<h3>.*?<a.*?>(.*?)</a>', re.M | re.S)
    # 新闻链接
    pat3 = re.compile(r'<h3>.*?<a.*?href="(.*?)"', re.M | re.S)
    # tag文本
    pat4 = re.compile(r'<div.*?class="keywords">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', re.M | re.S)
    # 跟帖数
    pat5 = re.compile(r'<a.*?class="comment">.*?<span.*?class="icon">(.*?)</span>', re.M | re.S)
    for page in range(1, 11):
        if page == 1:
            url = 'http://sports.163.com/zc/'
        else:
            if page < 10:
                str_page = '0' + str(page)
            else:
                str_page = str(page)
            url = 'https://sports.163.com/special/00051C89/zc_' + str_page + '.html'
        print('page:', page)
        html = down(url)
        # print(html)
        # 数据提取
        ls = pat1.findall(html)
        print('len:', len(ls))
        for item in ls:
            # print('item:',item)
            # 标题
            match_obj = pat2.search(item)
            if match_obj != None:
                title = match_obj.group(1)
            else:
                title = '空'
            print('title:', title)
            # 新闻链接
            match_obj = pat3.search(item)
            if match_obj != None:
                news_url = match_obj.group(1)
            else:
                news_url = '空'
            print('news_url:', news_url)
            # tag文本
            match_obj = pat4.search(item)
            if match_obj != None:
                tags = match_obj.group(1) + ' ' + match_obj.group(2)
            else:
                tags = '空'
            print('tags:', tags)
            # 跟帖数
            match_obj = pat5.search(item)
            if match_obj != None:
                nums = match_obj.group(1)
            else:
                nums = '0'
            print('nums:', nums)
            print('=' * 200)
            # 存储
            data = {
                'title': title,
                'news_url': news_url,
                'tags': tags,
                'nums': nums
            }
            data = json.dumps(data)  # dict===>字符串
            r.lpush('zc1911', data)
