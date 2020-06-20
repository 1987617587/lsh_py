# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from day14.peoplespider.peoplespider.items import PeoplespiderItem


class PeopleSpider(RedisCrawlSpider):
    name = 'people'
    redis_key = 'people:start_urls'
    # 匹配翻页链接
    link_page = LinkExtractor(restrict_xpaths=('//div[contains(@class,"page_n ")]/a'))
    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//ul[contains(@class,"mt10")]/li/a'))
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
        super(PeopleSpider, self).__init__(*args, **kwargs)



    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        # print(response.url)
        # 获取详情页数据
        title = response.xpath('//h1/text()').extract()[0].strip()
        detail_url = response.url
        detail_text = response.xpath('//div[@class="box_con"]//text()').extract()
        # 文本列表转字符串并删除空格
        detail_text = ''.join(detail_text).strip()
        detail_text = detail_text.replace('\n','')
        detail_text = detail_text.replace('\t\u3000\u3000','')
        pub_date = response.xpath('//div[@class="box01"]/div[@class="fl"]/text()').extract()[0].strip()
        source = response.xpath('//div[@class="box01"]/div[@class="fl"]/a/text()').extract()[0].strip()
        self.log(f'title:{title}')
        self.log(f'detail_url:{detail_url}')
        self.log(f'detail_text:{detail_text}')
        self.log(f'pub_date:{pub_date}')
        self.log(f'source:{source}')
        # 存储
        item = PeoplespiderItem()
        item['title']=title
        item['detail_url']=detail_url
        item['detail_text']=detail_text
        item['pub_date']=pub_date
        item['source']=source

        # 把提交给管道pipeline
        yield item
