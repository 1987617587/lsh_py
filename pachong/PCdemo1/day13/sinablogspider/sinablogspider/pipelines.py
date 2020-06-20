# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv


class SinablogspiderPipeline(object):

    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('sina_blog.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['标题', '链接'])

    def process_item(self, item, spider):
        self.wr.writerow([item['title'], item['url']])
        return item

    def close_spider(self, spider):
        self.file.close()

