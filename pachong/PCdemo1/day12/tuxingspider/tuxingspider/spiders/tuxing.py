# -*- coding: utf-8 -*-
import json

import scrapy

from day12.tuxingspider.tuxingspider.items import TuxingspiderItem


class TuxingSpider(scrapy.Spider):
    name = 'tuxing'
    allowed_domains = ['photophoto.cn']
    start_urls = ['http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5/']
    offset = 1

    def parse(self, response):

        self.url = 'http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5/'
        print(f'page:{self.offset}')
        # print(response.text)
        # 提取海报条目的列表
        photo_list = response.xpath('//ul[@id="list"]/li')
        print(f'len:{len(photo_list)}')

        for each in photo_list:
            detail_url = 'http:' + each.xpath('.//div[@class="image"]/a/@href').extract()[0].strip()
            # print(f'detail_url:{detail_url}')
            req = scrapy.Request(detail_url, callback=self.parse_detail)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        # 翻译操作 可以寻找url的规律也可以查找下一页按钮的href
        if self.offset <= 3:
            self.offset += 1
            next_page_url = self.url + '1-0-0-0-0-2-0-' + str(self.offset) + '.html'
            # next_page_url = 'http://so.photophoto.cn'+response.xpath('//div[@id="page"]/div[@class="pagenext"]/a/@href').extract()[0]
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        # print(response.text)
        print(response.url)

        # 标题
        title = response.xpath('//h1/text()').extract()[0].strip()
        print(f'title:{title}')

        # 图片地址
        image_url = 'http:' + response.xpath('//div[@id="photo"]/img/@src').extract()[0].strip()
        print(f'image_url:{image_url}')

        item = TuxingspiderItem()
        item['name'] = title
        item['image_url'] = image_url
        # 把提交给管道pipeline
        yield item
