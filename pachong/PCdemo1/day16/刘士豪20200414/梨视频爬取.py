# author:lsh
# datetime:2020/4/14 17:32 
'''
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
                                                                                                     
            '''
import os
import re

import requests
import time
import random
import json
import xlwt  # excel文档的写操作
def down_video(url,path):
    with requests.get(url,stream=True) as response: # 使用字节流的方式下载
        print('开始下载视频……')
        # 数据块的大小
        chunk_size = 10240
        # 获取视频的大小
        content_size = int(response.headers['content-length'])
        print(f'content_size:{content_size}')
        with open(path,'wb')as file:
            n = 1
            for chunk in response.iter_content(chunk_size=chunk_size):
                loaded = n*chunk_size / content_size
                print(f'已下载：{loaded:%}')
                n += 1
                file.write(chunk)
    print("下载成功")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/category_8',
    'Cookie':'__secdyid=84f00d239b16acbdcfb9cde101a17af47b0d99ea9a3a759a021586856771; JSESSIONID=9BC77A296B4EA4B8841EC7857515E446; PEAR_UUID=63dcb5e7-c77d-4312-b9ee-b74afd0cb7cd; PV_WWW=srv-pv-prod-portal4; _uab_collina=158685677096523995133632; UM_distinctid=1717808bfe41ee-08084333e12f5a-b791b36-1fa400-1717808bfe642d; CNZZDATA1260553744=996779612-1586856014-https%253A%252F%252Fwww.baidu.com%252F%7C1586856014; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1586856772; __ads_session=zQ/j+u9ZdQk+8LohtQA=; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1586856796'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/',
    'Cookie':'__secdyid=84f00d239b16acbdcfb9cde101a17af47b0d99ea9a3a759a021586856771; JSESSIONID=9BC77A296B4EA4B8841EC7857515E446; PEAR_UUID=63dcb5e7-c77d-4312-b9ee-b74afd0cb7cd; PV_WWW=srv-pv-prod-portal4; _uab_collina=158685677096523995133632; UM_distinctid=1717808bfe41ee-08084333e12f5a-b791b36-1fa400-1717808bfe642d; CNZZDATA1260553744=996779612-1586856014-https%253A%252F%252Fwww.baidu.com%252F%7C1586856014; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1586856772; __ads_session=zQ/j+u9ZdQk+8LohtQA=; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1586856796'
}

# url = 'https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=12&mrd=0.5616803019773882&filterIds=1668776,1668820,1667839,1667761,1668006,1667974,1667846,1667598,1667770,1667134,1667302,1667266'

# 把上面路由优化，修改参数，进行多页爬取
pageCount = 1
# url = 'https://www.pearvideo.com/category_8'
url = 'https://www.pearvideo.com/category_loading.jsp'

# for page in range(5):
page = 0
while page<= pageCount:
    print(f'page:{page}')
    params = {
        'reqType': '5',
        'categoryId': '8',
        'start': page*12,
    }
    page+=1

    response = requests.get(url, params=params, headers=headers)
    html = response.text
    # print(html)
    pat = re.compile(r'<a.*?href="(.*?)" class="vervideo-lilink actplay">')
    ls = pat.findall(html)
    # ['video_1668820', 'video_1668776', 'living_1667761', 'video_1667839', 'video_1668006', 'video_1667974', 'video_1667846', 'video_1667598', 'video_1667770', 'video_1667134', 'video_1667302', 'video_1667266']
    print(ls)
    for detail_url in ls:
        video_detail_url = 'https://www.pearvideo.com/'+detail_url
        print(f'video_detail_url:{video_detail_url}')
        headers2['Referer'] = 'https://www.pearvideo.com/'+detail_url
        print(headers2)
        response = requests.get(video_detail_url,headers=headers2)

        print(response.text)
        detail_html = response.text
        pat = re.compile(r'.*?srcUrl="(.*?)"')
        mp4_url = pat.findall(detail_html)[0]

        print(f'mp4_url:{mp4_url}')
        # 开始下载视频
        down_video(mp4_url,'videos/'+os.path.basename(mp4_url))


    time.sleep(random.random())


