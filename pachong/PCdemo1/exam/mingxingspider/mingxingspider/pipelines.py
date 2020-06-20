# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MingxingspiderPipeline(object):
    '''
    实现mysql数据的存储
    '''

    def __init__(self):
        '''
        初始化，建立数据库连接
        '''
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
        self.cur = self.conn.cursor()
        print("数据库连接成功")

    def process_item(self, item, spider):
        strsql = 'insert into mingxing values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = [item['name'], item['English_name'], item['blood_type'], item['country'], item['height'],
                  item['weight'], item['birthday'], item['graduation_school'], item['birthplace'],
                  item['constellation'], item['introduction'],item['TV'], item['film']]
        self.cur.execute(strsql, params)
        self.conn.commit()
        print("存储成功")

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
