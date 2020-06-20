#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests # 页面抓取的库
from lxml import etree  # 数据解析提取的库
import pymysql # 存储
import time # 随机延迟
import random

def down(url):
    '''
    下载制定url的页面
    :param url:
    :return:
    '''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    html = response.content
    return html


if __name__=="__main__":
    try:
        conn = pymysql.connect(host='192.168.1.119',port=3306,user='lsh',password='123456',db='good')
        cur = conn.cursor()
    except Exception as e:
        print(e)

    for page in range(1,50):
        # 1、页面抓取
        if page == 1:
            url = 'https://sh.lianjia.com/ershoufang/'
        else:
            url = 'https://sh.lianjia.com/ershoufang/pg'+str(page)+'/'
        print('page:',page)
        html = down(url)
        #print(html)
        # 2#、数据提取
        html = etree.HTML(html)
        ls = html.xpath('//ul[@class="sellListContent"]/li//div[@class="title"]/a/@href')
        print('len:',len(ls))
        for link in ls:
            print('link:',link)
            # 请求详情页面
            detail_html = down(link)
            detail_html = etree.HTML(detail_html)
            # 标题
            title = detail_html.xpath('//h1[@class="main"]/text()')[0]
            print('title:',title)
            # 详情链接
            detail_url = link
            print('detail_url:',detail_url)
            # 均价
            unit_price = detail_html.xpath('//span[@class="unitPriceValue"]/text()')[0]
            print('unit_price:',unit_price)
            # 单位
            unit = detail_html.xpath('//span[@class="unitPriceValue"]/i/text()')[0]
            print('unit:',unit)
            # 总价
            total_price = detail_html.xpath('//div[@class="price "]/span[@class="total"]/text()')[0]
            print('total_price:',total_price)
            # 总价单位
            total_unit = detail_html.xpath('//div[@class="price "]/span[@class="unit"]/span/text()')[0]
            print('tatal_unit:',total_unit)
            # 小区名称
            name = detail_html.xpath('//div[@class="communityName"]/a[@class="info "]/text()')[0]
            print('name:',name)
            # 区域
            region = detail_html.xpath('//div[@class="areaName"]/span[@class="info"]//text()')
            region = ' '.join(region)
            print('region:',region)
            # 基本信息
            bases = detail_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li')
            roomtype=bases[0].xpath('./text()')[0]
            print('roottype:',roomtype)
            floors = bases[1].xpath('./text()')[0]
            print('floors:', floors)
            area = bases[2].xpath('./text()')[0]
            print('area:', area)
            rootstruct = bases[3].xpath('./text()')[0]
            print('rootstruct:', rootstruct)
            withinarea = bases[4].xpath('./text()')[0]
            print('withinarea:', withinarea)
            buildtype = bases[5].xpath('./text()')[0]
            print('buildtype:', buildtype)
            roomdir = bases[6].xpath('./text()')[0]
            print('roomdir:', roomdir)
            buildstruct = bases[7].xpath('./text()')[0]
            print('buildstruct:', buildstruct)
            decrator = bases[8].xpath('./text()')[0]
            print('decrator:', decrator)
            elevator = bases[9].xpath('./text()')[0]
            print('elevator:', elevator)
            haselevator = bases[10].xpath('./text()')[0]
            print('haselevator:', haselevator)
            intrest = bases[11].xpath('./text()')[0]
            print('intrest:', intrest)
            print('='*200)
            # 3、数据存储
            strsql = 'insert into lianjia VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            params = [title,detail_url,unit_price,unit,total_price,total_unit,name,region,roomtype,floors,area,rootstruct,withinarea,buildtype,roomdir,buildstruct,decrator,elevator,haselevator,intrest]
            cur.execute(strsql,params)
            conn.commit()
            # 随机延迟
            time.sleep(random.random())
    cur.close()
    conn.close()

