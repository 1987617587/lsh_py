'''
level
2:
案例：steam游戏爬虫
https://store.steampowered.com/search/?os=win&filter=globaltopsellers
爬取游戏名称，链接，发布日期，价格，封面链接

'''

import json
import re
import time, random
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Cookie': 'browserid=1583519136134043099; timezoneOffset=28800,0; _ga=GA1.2.286001437.1585136894; recentapps=%7B%2212210%22%3A1585139106%7D; steamCountry=CN%7C5f5d50facb921b2c63f83bc655663d9b; sessionid=381c33614d8012f31c1256e5; _gid=GA1.2.1098869448.1585911359; app_impressions=346110@1_7_7_globaltopsellers_150_1|578080@1_7_7_globaltopsellers_150_1|782330@1_7_7_globaltopsellers_150_1|1100600@1_7_7_globaltopsellers_150_1|976730:1064220:1064221:1064270:1064271:1064272:1064273@1_7_7_globaltopsellers_150_1|952060@1_7_7_globaltopsellers_150_1|261550@1_7_7_globaltopsellers_150_1',
    'Referer': 'https://store.steampowered.com/search/?os=win&filter=globaltopsellers'
}
url = 'https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
# 加入循环，多页获取
for page in range(1,5):
    print(f"page:{page}")

    params = {
        'start': 50*page,
        'count': 50,
        'dynamic_data':'' ,
        'sort_by': '_ASC',
        'os': 'win',
        'snr': '1_7_7_globaltopsellers_7',
        'filter': 'globaltopsellers',
        'infinite': 1,
    }
    html = requests.get(url, params=params, headers=headers).text
    # print(html)
    # 把html的值提取处理（他是一个html文本,但是还是有些乱码）
    html = html.replace(r'&quot;', '')
    html = html.replace('\\', '')

    pat = re.compile(r'"results_html":"(.*?)","total_count"')
    html_text = pat.search(html).group(1)
    # print(html_text)

    # 存储一下，方便查看
    with open('steam'+str(page)+'.html', 'w', encoding='utf-8') as file:
        file.write(html_text)

    # 对处理后的html文本进行解析
    html = etree.HTML(html_text)
    ls = html.xpath('//a[contains(@class,"search_result_row")]')
    print(f'len:{len(ls)}')
    for each in ls:
        # 游戏名称
        title = each.xpath('.//span[@class="title"]/text()')[0]
        print(f'title:{title}')
        # 链接
        detail_url = each.xpath('.//@href')[0]

        print(f'detail_url:{detail_url}')
        # 发布日期
        pub_date = each.xpath('.//div[contains(@class,"search_released")]/text()')
        if pub_date:
            pub_date = pub_date[0]
            print(f'pub_date:{pub_date}')
        # 价格
        price = each.xpath('.//div[contains(@class,"search_price")]/text()')[0]
        print(f'price:{price}')
        # 封面链接
        cover_link= each.xpath('.//div[contains(@class,"search_capsule")]/img/@src')[0]
        print('cover_link:', cover_link)
        print('='*33)
