# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from day14.dhxyspider.dhxyspider.items import DhxyspiderItem


class DhxySpider(RedisCrawlSpider):
    name = 'dhxy'

    redis_key = 'dhxy:start_urls'

    # 匹配翻页链接 可以使用re,css,xpath
    link_page = LinkExtractor(restrict_xpaths=('//span[@class="pagebox_next"]/a'))

    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//div[@class="hot_wrap"]/ul/li/a'))
    # 定义规则
    rules = [
        Rule(link_page, follow=True),
        Rule(link_item, callback='parse_detail', follow=False)
    ]

    def __init__(self, *args, **kwargs):
        # 动态设置允许爬取页面的域
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(DhxySpider, self).__init__(*args, **kwargs)

    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        # print(response.text)
        # print(response.url)
        # 获取详情页数据
        title = response.xpath('//h1[@class="F-yahei"]/text()').extract()[0].strip()
        detail_url = response.url
        detail_text = response.xpath('//div[@id="fonttext"]//text()').extract()
        detail_text = ''.join(detail_text).strip()
        # pub_date = response.xpath('//div[@class="lightgray F-song txtdetail"]//text()')
        pat = re.compile(
            r'([1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d)')
        pub_date = pat.findall(response.text)[0][0]

        source = response.xpath('//div[@class="lightgray F-song txtdetail"]/a/text()').extract()[0].strip()
        self.log(f'title:{title}')
        self.log(f'detail_url:{detail_url}')
        self.log(f'detail_text:{detail_text}')
        self.log(f'pub_date:{pub_date}')
        self.log(f'source:{source}')
        # 存储
        item = DhxyspiderItem()
        item['title'] = title
        item['detail_url'] = detail_url
        item['detail_text'] = detail_text
        item['pub_date'] = pub_date
        item['source'] = source

        # 把提交给管道pipeline
        yield item
