# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv

import pymysql


class Task2Pipeline(object):

    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('people.csv','w',encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['标题','链接','内容','发布时间','来源'])


    def process_item(self, item, spider):
        self.wr.writerow([item['title'],item['detail_url'],item['detail_text'],item['pub_date'],item['source']])
        return item

    def close_spider(self,spider):
        self.file.close()


# 新建管道
class Task2MysqlPipeline(object):
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
        strsql = 'insert into people values(0,%s,%s,%s,%s,%s)'
        params = [item['title'],item['detail_url'],item['detail_text'],item['pub_date'],item['source']]
        self.cur.execute(strsql, params)
        self.conn.commit()
        print("存储成功")

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()