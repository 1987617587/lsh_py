# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
'''
心通桥（spider）
https://xtq.zynews.cn/wzpostlist.php?mod=list
爬去投诉帖子的标题，链接，内容，投诉者，投诉时间
存储到mysql数据库
'''

class Task3Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail_url = scrapy.Field()
    detail_text = scrapy.Field()
    complainant = scrapy.Field()
    pub_date = scrapy.Field()

