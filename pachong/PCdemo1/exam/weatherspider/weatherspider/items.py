# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # Province, city, weather, maximum temperature, minimum temperature, date
    province = scrapy.Field()
    city = scrapy.Field()
    weather = scrapy.Field()
    max_temperature = scrapy.Field()
    min_temperature = scrapy.Field()
    pub_date = scrapy.Field()
