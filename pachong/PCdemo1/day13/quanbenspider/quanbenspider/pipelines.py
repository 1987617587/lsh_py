# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv


# 爬取小说名称，url，类别，作者，更新时间，状态

class QuanbenspiderPipeline(object):
    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('quanben.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['小说名称', '链接', '类别', '作者', '更新时间', '状态'])

    def process_item(self, item, spider):
        self.wr.writerow(
            [item['name'], item['url'], item['category'], item['author'], item['update_time'], item['status']])
        return item

    def close_spider(self, spider):
        self.file.close()
