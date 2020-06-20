# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from day13.yuanzunspider.yuanzunspider.items import YuanzunspiderItem


class YuanzunSpider(CrawlSpider):
    name = 'yuanzun'
    allowed_domains = ['biquge.info']
    start_urls = ['http://www.biquge.info/0_383/']


    # 匹配翻页链接 可以使用re,css,xpath
    # link_page = LinkExtractor(restrict_xpaths=('//a[@class="nxt"]'))
    # link_page = LinkExtractor(restrict_css='a.next')
    # 使用正则不用担心匹配可能会重复，自带去重
    # link_page = LinkExtractor(allow=(r'wzpostlist\.php\?mod=list'))
    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//div[@id="list"]/dl/dd/a'))
    # 定义规则
    rules = [
        # Rule(link_item, callback='parse_list',follow=False)
        Rule(link_item, callback='parse_list',follow=True)
    ]

    def parse_list(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_list函数执行了')
        # print(response.url)
        # 获取详情页数据
        chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0].strip()
        chapter_url = response.url
        chapter_text = response.xpath('//div[@id="content"]//text()').extract()
        chapter_text = ''.join(chapter_text)

        # 提取内容


        self.log(f'chapter_name:{chapter_name}')
        self.log(f'chapter_url:{chapter_url}')
        self.log(f'chapter_text:{chapter_text}')

        # 存储

        item = YuanzunspiderItem()
        item['chapter_name'] = chapter_name
        item['chapter_url'] = chapter_url
        item['chapter_text'] = chapter_text

        # 把提交给管道pipeline
        yield item

