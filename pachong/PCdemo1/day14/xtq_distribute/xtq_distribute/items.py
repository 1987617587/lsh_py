# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XtqDistributeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    detail_url = scrapy.Field()
    detail_text = scrapy.Field()
    complainant = scrapy.Field()
    pub_date = scrapy.Field()
