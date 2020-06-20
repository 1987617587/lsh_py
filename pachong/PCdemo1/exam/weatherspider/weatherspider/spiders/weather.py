# -*- coding: utf-8 -*-
import scrapy

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from exam.weatherspider.weatherspider.items import WeatherspiderItem


class WeatherSpider(CrawlSpider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather1d/101180101.shtml']


    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//ul[@class="clearfix city"]/li/a'))
    # 定义规则
    rules = [
        Rule(link_item, callback='parse_detail', follow=True)
    ]

    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        # print(response.text)


        province = response.xpath('//div[@class="crumbs fl"]/a[2]/text()').extract()[0].strip()
        city = response.xpath('//div[@class="crumbs fl"]/a[3]/text()').extract()[0].strip()
        print(province, city)
        weather = response.xpath('//input[@id="hidden_title"]/@value').extract()[0].strip()
        print(weather)
        max_temperature = response.xpath('//div[@class="t"]/ul/li[1]/p[@class="tem"]/span/text()').extract()[0].strip()
        min_temperature = response.xpath('//div[@class="t"]/ul/li[2]/p[@class="tem"]/span/text()').extract()[0].strip()
        print(max_temperature, min_temperature)

        pub_date = response.xpath('//h1[@class="clearfix city"]/i/text()').extract()[0].strip()
        print(pub_date)

        # 存储
        item = WeatherspiderItem()
        item['province'] = province
        item['city'] = city
        item['weather'] = weather
        item['max_temperature'] = max_temperature
        item['min_temperature'] = min_temperature
        item['pub_date'] = pub_date

        # 把提交给管道pipeline
        yield item
