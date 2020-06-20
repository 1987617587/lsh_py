# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv,os


class YuanzunspiderPipeline(object):
    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('quanben.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['章节名称', '链接', '内容'])

    def process_item(self, item, spider):

        self.wr.writerow([item['chapter_name'], item['chapter_url'], item['chapter_text']])
        return item

    def close_spider(self, spider):
        self.file.close()

class YuanzuntxtspiderPipeline(object):


    def process_item(self, item, spider):
        with open('yuanzun/'+item['chapter_name']+'.txt', 'w', encoding='utf-8') as self.file:
            self.file.write(item['chapter_text'])

        return item

    def close_spider(self, spider):
        self.file.close()