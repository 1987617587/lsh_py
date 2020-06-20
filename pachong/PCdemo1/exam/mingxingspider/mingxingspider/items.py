# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MingxingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # Star name, English name, blood type, height, country, height, weight, birthday,
    # graduation school, birthplace, constellation, brief introduction, TV series works, film works
    name = scrapy.Field()
    English_name = scrapy.Field()
    blood_type = scrapy.Field()
    country = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    birthday = scrapy.Field()
    graduation_school = scrapy.Field()
    birthplace = scrapy.Field()
    constellation = scrapy.Field()
    introduction = scrapy.Field()
    TV = scrapy.Field()
    film = scrapy.Field()
