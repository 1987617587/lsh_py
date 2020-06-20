# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    name = scrapy.Field()
    # 招聘公司
    corp = scrapy.Field()
    # 工作地点
    city = scrapy.Field()
    # 薪资待遇
    salary = scrapy.Field()
    # 发布时间
    pud_date = scrapy.Field()
    # 岗位要求
    job_msg = scrapy.Field()
