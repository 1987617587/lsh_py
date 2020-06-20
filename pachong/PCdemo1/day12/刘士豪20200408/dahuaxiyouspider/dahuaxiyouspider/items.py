# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 爬取标题，日期，来源，攻略内容
import scrapy


class DahuaxiyouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pub_date = scrapy.Field()
    source = scrapy.Field()
    detail_text = scrapy.Field()
    detail_url = scrapy.Field()
