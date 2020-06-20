# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanbenspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url =  scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    update_time = scrapy.Field()
    status = scrapy.Field()


