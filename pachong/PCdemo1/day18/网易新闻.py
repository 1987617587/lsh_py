# author:lsh
# datetime:2020/4/16 16:57 
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
'''
爬取新闻标题，出处，发表时间，内容，id
'''
import os
import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作

headers = {
    'User-Agent': 'NewsApp/54.6 Android/4.4.2 (lenovo/Lenovo K8 Note)',
    'Accept-Encoding': 'gzip',

}
base_url = 'https://c.m.163.com'


def get_list():
    url = '/recommend/getSubDocPic?tid=T1348647909107&from=toutiao&offset=20&size=10&fn=1&LastStdTime=0&spestr=reader_expert_2&prog=&passport=&devId=03c9vBIFZVo5KrKhYbaQbw%3D%3D&lat=IiOkkNUqtAXXwTJomLrjgg%3D%3D&lon=nZc7dcCulYzaQLlRQGyxrQ%3D%3D&version=54.6&net=wifi&ts=1587027414&sign=%2BFybtYCNJgS2kpoSMfcTx96RNZvQXWbeBeblf6bHh1948ErR02zJ6%2FKXOnxX046I&encryption=1&canal=netease_gw&mac=Vq4RRC2MBTNLrBWuOmx5AWA6W63jXMiLLBRm8sTXwOw%3D&open=&openpath= HTTP/1.1'
    # params = {
    #     'reqType': '5',
    #     'categoryId': '8',
    #     'start': page * 12,
    # }

    # response = requests.get(url, params=params, headers=headers)
    response = requests.get(base_url + url, headers=headers)
    # html = response.text
    # print(html)
    # json格式
    data = response.json()
    print(data)
    news = data['T1348647909107']
    for each in news:
        print(each['docid'])
        print(each['title'])
        docid = each['docid']
        print(docid, type(docid))
        get_detail(docid)
        break


def get_detail(docid):
    # 详情页链接GET /nc/article/preload/FA1AVJM50515STP0/full.html HTTP/1.1
    detail_url = '/nc/article/preload/FABUDGQ600019B3E/full.html HTTP/1.1'

    # detail_url = f'/nc/article/preload/{docid}/full.html HTTP/1.1'
    response = requests.get(base_url + detail_url, headers=headers)
    data = response.json()[docid]
    print(data)
    # 爬取新闻标题，出处，发表时间，内容，id
    title = data['title']
    source = data['source']
    ptime = data['ptime']
    body = data['body']
    id = docid
    print(f'title:{title}')
    print(f'source:{source}')
    print(f'ptime:{ptime}')
    print(f'body:{body}')
    print(f'id:{id}')


if __name__ == '__main__':
    get_list()
