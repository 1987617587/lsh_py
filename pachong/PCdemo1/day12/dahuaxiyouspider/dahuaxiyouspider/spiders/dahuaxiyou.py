# -*- coding: utf-8 -*-
import re

import scrapy

from day12.dahuaxiyouspider.dahuaxiyouspider.items import DahuaxiyouspiderItem


class DahuaxiyouSpider(scrapy.Spider):
    name = 'dahuaxiyou'
    allowed_domains = ['97973.com']
    start_urls = ['http://search.97973.com/guides/search?search_key=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8']
    page = 1
    max_pages = 3

    def parse(self, response):
        print('parse函数执行了--',self.page)
        # print(response.text)
        # 提取攻略条目的列表
        strategy_list = response.xpath('//div[@class="hot_wrap"]/ul/li')
        print(f'len:{len(strategy_list)}')
        for each in strategy_list:

            # 详情链接
            detail_url =  each.xpath('./a/@href').extract()[0].strip()
            self.log(f'detail_url:{detail_url}')
            req_detail = scrapy.Request(detail_url, callback=self.parse_content)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req_detail

        # 翻页处理

        self.page += 1
        if self.page <= self.max_pages:
            url = 'http://search.97973.com/guides/search?search_key=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8&page='+str(self.page)
            print(f'page:{self.page},url:{url}')
            # 生成请求对象
            req = scrapy.Request(url, callback=self.parse)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

    def parse_content(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        print(response.text)
        # print(response.url)
        # 获取详情页数据
        title = response.xpath('//h1[@class="F-yahei"]/text()').extract()[0].strip()
        detail_url = response.url
        detail_text = response.xpath('//div[@id="fonttext"]//text()').extract()
        detail_text = ''.join(detail_text).strip()
        # pub_date = response.xpath('//div[@class="lightgray F-song txtdetail"]//text()')
        pat = re.compile(r'([1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d)')
        pub_date = pat.findall(response.text)[0][0]
        # if pub_date:
        #     pub_date = pub_date.extract()[0].strip()
        # else:
        #     pub_date = '暂未获取'
        source = response.xpath('//div[@class="lightgray F-song txtdetail"]/a/text()').extract()[0].strip()
        self.log(f'title:{title}')
        self.log(f'detail_url:{detail_url}')
        self.log(f'detail_text:{detail_text}')
        self.log(f'pub_date:{pub_date}')
        self.log(f'source:{source}')
        # 存储
        item = DahuaxiyouspiderItem()
        item['title'] = title
        item['detail_url'] = detail_url
        item['detail_text'] = detail_text
        item['pub_date'] = pub_date
        item['source'] = source

        # 把提交给管道pipeline
        yield item

