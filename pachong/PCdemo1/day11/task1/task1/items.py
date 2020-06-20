# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

'''
b站排行榜爬虫（scrapy）
https://www.bilibili.com/ranking#!/all/0/0/7/
爬取编号，标题，url，综合评分，播放量，评论数
存储到mysql数据库
'''
class Task1Item(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    playback_volume = scrapy.Field()
    comments = scrapy.Field()
    author = scrapy.Field()


