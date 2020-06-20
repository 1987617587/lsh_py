import json
import re
import time,random
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Cookie': 'PSTM=1583895540; BIDUPSID=C92D780B805E9621887192AB4135A9D5; sug=3; ORIGIN=0; bdime=0; BAIDUID=15F6AA3C5B2E63BA787D2BD038F1BBBD:SL=0:NR=10:FG=1; MCITY=-%3A; H_WISE_SIDS=140842_142081_143803_142062_142112_141910_143390_143856_143879_141747_142512_139171_141900_142780_136862_131246_142909_141261_138165_138883_140259_141942_127969_142872_140065_143998_140593_143059_143492_131953_140351_143468_143922_143275_131423_144003_107315_138595_143959_143477_142911_142273_110085; BD_UPN=12314753; BDUSS=9qRFM1RGFoNWtMMjRrY3RGMHF2ZHI5LUVma3FPQWhiWTRhMkt5S3ZMUWhRYXBlRVFBQUFBJCQAAAAAAAAAAAEAAABJhg6pusC45zE5ODc2MTc1ODcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACG0gl4htIJeQ0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; COOKIE_SESSION=121_0_9_7_1_9_0_0_9_5_1_0_0_0_0_0_1585814510_0_1585885363%7C9%237943_22_1584691567%7C6; BD_HOME=1; BDRCVFR[IZdXtXdDRBm]=OjjlczwSj8nXy4Grjf8mvqV; H_PS_PSSID=; sugstore=1'

}
# url = 'https://www.baidu.com/home/pcweb/data/mancardwater?id=2&offset=11&sessionId=15858962504121&crids=&version=&pos=63&newsNum=63&blacklist_timestamp=0&indextype=manht&_req_seqid=0xf00c0e7900050799&asyn=1&t=1585896446512&sid=1420_31169_21115_30840_31186_30908_30824_31086_26350_31163_28704'
url = 'https://www.baidu.com/home/pcweb/data/mancardwater'
# 加入循环，多页获取
for page in range(1,5):
    print(f"page:{page}")
    params = {
        'id': 2,
        'offset': page,
        'sessionId': 15858962504121,
        'crids': '',
        'version': '',
        'pos': (2*page-1)*3,
        'newsNum': (2*page-1)*3,
        'blacklist_timestamp': 0,
        'indextype': 'manht',
        '_req_seqid': 0xf00c0e7900050799,
        'asyn': 1,
        # 't': 1585896445313,
        't': int(time.time()*1000),
        'sid': 1420_31169_21115_30840_31186_30908_30824_31086_26350_31163_28704,
    }

    html = requests.get(url, params=params,headers=headers).text
    # print(html)
    # 把html的值提取处理（他是一个html文本,但是还是有些乱码）
    html = html.replace(r'\x22', '"')
    html = html.replace(r'&quot;', '')
    pat = re.compile(r'"html" : "(.*?)","isEnd"')
    html_text = pat.search(html).group(1)
    # print(html_text)
    # data = json.loads(html)
    # 存储一下，方便查看
    with open('baidu.html', 'w', encoding='utf-8') as file:
        file.write(html_text)

    # 对处理后的html文本进行解析
    html = etree.HTML(html_text)
    ls = html.xpath('//div[contains(@class,"s-news-special")]')
    print(f'len:{len(ls)}')
    for each in ls:
        title = each.xpath('.//h2/a/@title')[0]
        print(f'title:{title}')
        detail_url = each.xpath('.//h2/a/@href')[0]
        detail_url = detail_url.replace('\/', '/')
        print(f'detail_url:{detail_url}')
        src_net = each.xpath('.//span[@class="src-net"]/a/text()')[0]
        src_net = src_net.replace(r'\r\n', '').strip()

        print(f'src_net:{src_net}')
        src_time = each.xpath('.//span[@class="src-time"]/text()')[0]
        src_time = src_time.replace(r'\r\n', '').strip()
        print(f'src_time:{src_time}')
        print('='*33)
