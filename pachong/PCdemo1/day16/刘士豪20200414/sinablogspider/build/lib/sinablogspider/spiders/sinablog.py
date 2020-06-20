# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from sinablogspider.items import SinablogspiderItem


class SinablogSpider(CrawlSpider):
    name = 'sinablog'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    link_page = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))


    rules = [
        Rule(link_page,callback='parse_list', follow=True),

    ]



    def parse_list(self, response):
        print('parse_list')
        # print(response.text)
        # 提取信息条目的列表
        ls = response.xpath('//span[@class="atc_title"]')
        print(f'len{len(ls)}')
        for each in ls:
            item = SinablogspiderItem()

            item['title'] = each.xpath('./a/text()').extract()[0].strip()
            item['url'] = each.xpath('./a/@href').extract()[0]
            yield item