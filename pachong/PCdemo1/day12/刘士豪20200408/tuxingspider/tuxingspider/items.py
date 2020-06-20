# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
'''
level 2:
图行天下图片爬虫
http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5
爬取海报图片保存到 images 目录下

'''
import scrapy


class TuxingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 存储照片的名字
    image_url = scrapy.Field()  # 照片的 url 路径
    image_path = scrapy.Field()  # 照片保存在本地的路径

