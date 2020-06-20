# author:lsh
# datetime:2020/4/15 20:48 
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
案例：六间房小视频下载
'''
import os
import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作

import requests


def get_list():
    max_page = 5
    page = 0
    while page <= max_page:
        page += 1
        headers = {
            'User-Agent': 'Xc27CgIxEEbhV)EFXP6Z3NNtISislYhYLTOJ0RW0Eyzy8GprdbrvvJdXucnz(pD7IvP5MLshDb5Hb(AtCBHsYPv2OJ42u9V(GtfjROgMZu7mV8CSowBPTooxVYtHJVViIakWzV5a0arSAigmZ79uCqKetceMzCG3krlldf)bDw@@',
        }
        base_url = 'http://v.6.cn'
        url = '/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php& HTTP/1.1'
        params = {
            'stpageart': page,
        }

        response = requests.get(base_url + url, params=params, headers=headers)
        # html = response.text
        # print(html)
        # json格式
        data = response.json()
        ls = data['content']['list']
        print(ls)
        for each in ls:
            alias = each['alias']
            print(f'alias:{alias}')
            playurl = each['playurl']
            print(f'playurl:{playurl}')
            path = os.path.basename(playurl)
            down_video(playurl, path)

            print('=' * 100)

    time.sleep(random.random())


def down_video(url, path):
    with requests.get(url, stream=True) as response:  # 使用字节流的方式下载
        print('开始下载视频……')
        # 数据块的大小
        chunk_size = 1024
        with open('videos/' + path, 'wb')as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
    print("下载成功")


if __name__ == '__main__':
    get_list()
