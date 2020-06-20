# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YuanzunspiderItem(scrapy.Item):
    # define the fields for your item here like:
    chapter_name = scrapy.Field()
    chapter_url = scrapy.Field()
    chapter_text = scrapy.Field()

