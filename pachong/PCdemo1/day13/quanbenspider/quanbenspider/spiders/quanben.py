# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from day13.quanbenspider.quanbenspider.items import QuanbenspiderItem


class QuanbenSpider(CrawlSpider):
    name = 'quanben'
    allowed_domains = ['quanben.net']
    start_urls = ['https://www.quanben.net/list/2_1.html']

    # 匹配翻页链接 可以使用re,css,xpath
    link_page = LinkExtractor(restrict_xpaths=('//a[@class="next"]'),unique=True)

    # 定义规则
    rules = [
        Rule(link_page,callback='parse_list', follow=True),
    ]

    def parse_list(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        print(response.text)
        # print(response.url)
        # 获取数据
        ls = response.xpath('//ul[@class="item-con"]/li')
        print(f'len{len(ls)}')
        for each in ls:



            name = each.xpath('./span[@class="s2"]/a/text()').extract()[0].strip()
            url = each.xpath('./span[@class="s2"]/a/@href').extract()[0]

            category = each.xpath('./span[@class="s1"]/text()').extract()[0].strip()
            author = each.xpath('./span[@class="s3"]/text()').extract()[0].strip()
            update_time = each.xpath('./span[@class="s4"]/text()').extract()[0].strip()

            status = each.xpath('./span[@class="s5"]/text()').extract()[0].strip()

            # # 存储
            item = QuanbenspiderItem()
            item['name'] = name
            item['url'] = 'https://www.quanben.net/'+url
            item['category'] = category
            item['author'] = author
            item['update_time'] = update_time
            item['status'] = status
            # 把提交给管道pipeline
            yield item
