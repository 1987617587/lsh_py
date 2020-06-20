# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
'''
人民网（scrapy）
http://politics.people.com.cn/GB/1024/index1.html
爬取新闻标题，链接，内容，发表时间'''

class Task2Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail_url = scrapy.Field()
    detail_text = scrapy.Field()
    pub_date = scrapy.Field()
    source = scrapy.Field()


