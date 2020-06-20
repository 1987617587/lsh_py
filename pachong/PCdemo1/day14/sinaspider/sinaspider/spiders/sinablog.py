# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from day14.sinaspider.sinaspider.items import SinaspiderItem


class SinablogSpider(RedisCrawlSpider):
    name = 'sinablog'
    redis_key = 'sina:start_urls'

    link_page = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))

    rules = [
        Rule(link_page, callback='parse_list', follow=True),
    ]

    def __init__(self, *args, **kwargs):
        # 动态设置允许爬取页面的域
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SinablogSpider, self).__init__(*args, **kwargs)

    def parse_list(self, response):
        print('parse_list')
        # print(response.text)
        # 提取信息条目的列表
        ls = response.xpath('//span[@class="atc_title"]')
        print(f'len{len(ls)}')
        for each in ls:
            item = SinaspiderItem()

            item['title'] = each.xpath('./a/text()').extract()[0].strip()
            item['url'] = each.xpath('./a/@href').extract()[0]
            yield item
