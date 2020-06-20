import requests
import time
import random
import xlwt  # excel文档的写操作

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

# 生成workbook 对象  execl文档的对象
xls = xlwt.Workbook()
# 新建execl文档中的sheet
sheet1 = xls.add_sheet('movie')
# 添加字段标题
sheet1.write(0, 0, 'id')
sheet1.write(0, 1, '标题')
sheet1.write(0, 2, '评分')
sheet1.write(0, 3, '链接')
sheet1.write(0, 4, '封面图片')
sheet1.write(0, 5, '导演')
sheet1.write(0, 6, '主演')

row = 1

for page in range(5):
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
        print(f'rate:{rate}')
        detail_url = each['url']
        print(f'detail_url:{detail_url}')
        cover = each['cover']
        print(f'cover:{cover}')
        directors = each['directors']
        directors = ''.join(directors)
        print(f'directors:{directors}')
        casts = each['casts']
        casts = ''.join(casts)
        print(f'casts:{casts}')
        print('=' * 100)
        # 存储数据
        sheet1.write(row, 0, id)
        sheet1.write(row, 1, title)
        sheet1.write(row, 2, rate)
        sheet1.write(row, 3, detail_url)
        sheet1.write(row, 4, cover)
        sheet1.write(row, 5, directors)
        sheet1.write(row, 6, casts)
        # 表格换行
        row += 1
    time.sleep(random.random() + 1)
xls.save('doubandanying.xls')