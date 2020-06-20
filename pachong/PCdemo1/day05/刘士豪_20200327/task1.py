"""
案例：笑话集爬虫（re）
http://www.jokeji.cn/hot.htm
爬取标题，浏览量，发表时间，内容


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
    # html = response.text
    html = response.content.decode(response.apparent_encoding, 'ignore')
    return html


if __name__ == '__main__':
    try:
        r = redis.StrictRedis(host='localhost', port=6379)
    except Exception as e:
        print(e)
    # 条目
    pat1 = re.compile(r'<table width="646".*?<tr>(.*?)</tr>', re.S | re.M)

    # 标题
    pat2 = re.compile(r'<td width="408".*?<a.*?>(.*?)</a>', re.S | re.M)
    # 浏览量
    pat3 = re.compile(r'<td width="124".*?(\d+)</td>', re.S | re.M)
    # 发表时间
    pat4 = re.compile(r'<td width="96".*?class="date">.*?(\d+)-(\d+)-(\d+).*?</span>', re.S | re.M)
    # 内容（详情页获取）
    # 详情连接
    pat5 = re.compile(r'<td width="408".*?<a.*?href="(.*?)".*?</a>', re.S | re.M)
    # 笑话内容
    pat6 = re.compile(r'<span id="text110">(.*?)</span>', re.S | re.M)
    for page in range(1, 11):
        if page == 1:
            url = 'http://www.jokeji.cn/hot.htm'
        else:
            if page < 10:
                str_page = '0' + str(page)
            else:
                str_page = str(page)
            url = 'http://www.jokeji.cn/hot.asp?me_page=' + str_page
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
            # 浏览量
            match_obj = pat3.search(item)
            if match_obj != None:
                nums = match_obj.group(1)
            else:
                nums = '0'
            print('nums:', nums)
            # 发表时间
            match_obj = pat4.search(item)
            if match_obj != None:
                pub_date = match_obj.group(1) + "-" + match_obj.group(2) + "-" + match_obj.group(3)
            else:
                pub_date = '空'
            print('pub_date:', pub_date)
            # 详情连接
            match_obj = pat5.search(item)
            if match_obj != None:
                # 拼接完整路径
                detail_url = "http://www.jokeji.cn" + match_obj.group(1)
            else:
                detail_url = '空'
            print('detail_url:', detail_url)
            # 文章内容
            # 请求详情页
            detail_html = down(detail_url)
            # print(html)
            # 数据提取
            # ls = pat1.findall(html)

            match_obj = pat6.search(detail_html)
            if match_obj != None:
                # 拼接完整路径
                joke_text = match_obj.group(1)
            else:
                joke_text = '空'
            print('joke_text:', joke_text)
            print('=' * 200)
            # 存储
            data = {
                'title': title,
                'nums': nums,
                'pub_date': pub_date,
                'joke_text': joke_text
            }
            data = json.dumps(data)  # dict===>字符串
            r.lpush('jokes', data)



# <a href="hot.asp?me_page=11"><img src="/images/Next.gif" border="0" alt="下十页"></a>
# 后十页页数获取注意转义字符的使用
# pat_page_nus = re.compile(r'<a.*?href="hot.asp\?me_page=(\d+)"><img.*?src="images/Next.gif"')