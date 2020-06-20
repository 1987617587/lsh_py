"""
level 3:
案例：爬取内涵吧爬虫（re）
https://www.neihan-8.com/wenzi//
正则表达式提取段子标题，url，点赞数，踩数，内容

"""
import random
import time

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


def get_text_list(url):
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
        # url
        match_obj = pat3.search(item)
        if match_obj != None:
            url = "https://www.neihan-8.com" + match_obj.group(1)
        else:
            url = '空'
        print('url:', url)
        # 点赞数
        match_obj = pat4.search(item)
        if match_obj != None:
            good_nums = match_obj.group(1)
        else:
            good_nums = '空'
        print('good_nums:', good_nums)
        # 踩数
        match_obj = pat5.search(item)
        if match_obj != None:
            bad_nums = match_obj.group(1)
        else:
            bad_nums = '空'
        print('bad_nums:', bad_nums)
        # 进入详情连接
        get_text_detail(url)

    # 下一页
    # 先来个随机延迟
    time.sleep(random.random())
    match_obj = pat7.search(html)
    if match_obj != None:
        next_page = match_obj.group(1)
    else:
        next_page = '空'
    print('next_page:', next_page)
    print('*:' * 66)
    get_text_list("https://www.neihan-8.com" + next_page)


def get_text_detail(detail_url):
    print("进入详情页", detail_url)

    # 文章内容
    # 请求详情页
    detail_html = down(detail_url)
    # print(detail_html)
    # 数据提取
    match_obj = pat6.search(detail_html)
    if match_obj != None:
        joke_text = match_obj.group(1)
    else:
        joke_text = '空'
    print('joke_text:', joke_text)
    print('=' * 200)



if __name__ == '__main__':
    try:
        r = redis.StrictRedis(host='localhost', port=6379)
    except Exception as e:
        print(e)
    # 条目，<div class="text-column-item box box-790">
    #         <h3><a href="/lxh/202629.html" class="title" title="超级灵药">超级灵药</a></h3>
    #         <div class="desc"> 　　
    #         汤姆早上老是睡过头，他的老板威胁说：如果再这样就要炒他鱿鱼。　　汤姆很着急，就去看医生，医生给了他一个药丸让他睡觉之前吃。　　这个晚上汤姆睡得很好，一大早就醒了，悠闲</div>
    #         <div class="bottom">
    #               <div class="time">
    #               <time class="timeago" datetime="2017-03-04.0">3年前</time>
    #               <i>属于：<a href="/lxh//" class="title">冷笑话</a></i>
    #               </div>
    #                 <div class="good">0</div>
    #                 <div class="bad">0</div>
    #                 <div class="view">54</div>
    #             </div>
    #       </div>
    # 可以在分组外描述匹配细节
    # pat1 = re.compile(r'<div class="text-column-item box box-790">(.*?)<div class="text-column-item box box-790">',
    #                   re.S | re.M)
    # 可以在分组中继续描述匹配细节
    pat1 = re.compile(r'(<div.*?class="text-column-item box box-790".*?class="view".*?</div>)', re.S | re.M)
    # 标题，<h3><a href="/lxh/202629.html" class="title" title="超级灵药">超级灵药</a></h3>
    # 通过标签内容获取标题
    # pat2 = re.compile(r'<h3.*?title="(.*?)"', re.S | re.M)
    # 通过文本获取标题
    pat2 = re.compile(r'<h3>.*?<a.*?>(.*?)</a>', re.S | re.M)
    # url，<div class="bottom">
    #               <div class="time">
    #               <time class="timeago" datetime="2017-03-04.0">3年前</time>
    #               <i>属于：<a href="/lxh//" class="title">冷笑话</a></i>
    #               </div>
    #                 <div class="good">0</div>
    #                 <div class="bad">1</div>
    #                 <div class="view">49</div>
    #             </div>
    pat3 = re.compile(r'<h3.*?href="(.*?)"', re.S | re.M)
    # 点赞数，
    pat4 = re.compile(r'<div class="good".*?(\d+)</div>', re.S | re.M)
    # 踩数
    pat5 = re.compile(r'<div class="bad".*?(\d+)</div>', re.S | re.M)

    # 内容（详情页获取）
    # 详情连接=url
    # 笑话内容
    pat6 = re.compile(r'<div class="detail".*?<p style="text-align: center;">(.*?)<div class="ad610"', re.S | re.M)

    # 有翻页url = 'https://www.neihan-8.com' + next_page
    # 递归调用获取
    # <a href="/wenzi//index_2.html" class="next">下一页</a>
    # 注意此时尽可能贪婪，拿到最后一个就是下一页
    pat7 = re.compile(r'<div class="pagenav".*<a href="(.*?)" class="next">', re.S | re.M)

    get_text_list("https://www.neihan-8.com/wenzi//")
