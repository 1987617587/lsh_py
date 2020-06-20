import codecs
import csv

import requests
import time
import random
import xlwt  # excel文档的写操作

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}


file = codecs.open('douban.csv', 'w', encoding='utf-8')
wr = csv.writer(file)
wr.writerow(['电影名称', '评分'])



for page in range(10):
    print('page:', page)
    url = 'https://movie.douban.com/j/new_search_subjects'
    params = {
        'sort': 'U',  # 排序的方式
        "range": "0,10",  # 电影评分的范围
        "tags": "电影,剧情,美国",  # 检索的标签
        # "playable": "1", # 是否可以播放
        "start": page * 20,  # 检索的开始位置 (这里可以去改变的 从 0 开始 一个电影代表的是一条数据)
        # "genres": "喜剧",  # 类型
        "countries": "中国大陆",  # 国家地区
        'year_range': '2019,2019',

    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    ls = data['data']
    print(f'len:{len}')
    results = []
    for each in ls:
        id = each['id']
        print(f'id:{id}')
        title = each['title']
        print(f'title:{title}')

        rate = each['rate']
        if not rate:
            rate = 0
        print(f'rate:{rate}')
        detail_url = each['url']
        # print(f'detail_url:{detail_url}')
        # cover = each['cover']
        # print(f'cover:{cover}')
        # directors = each['directors']
        # directors = ''.join(directors)
        # print(f'directors:{directors}')
        # casts = each['casts']
        # casts = ''.join(casts)
        # print(f'casts:{casts}')
        print('=' * 100)
        # 存储数据
        wr.writerow([title, rate])

    time.sleep(random.random() + 1)

file.close()