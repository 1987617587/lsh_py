# -*- coding: utf-8 -*-
import re

import scrapy

from day11.task2.task2.items import Task2Item


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['politics.people.com.cn']
    start_urls = ['http://politics.people.com.cn/GB/1024/index1.html']


    def __init__(self):
        self.page = 1
        self.max_pages = 3
        self.str_url  = 'http://politics.people.com.cn/GB/1024/index{}.html'

    def get_url(self):
        return self.str_url.format(self.page)


    def parse(self, response):
        '''
        进行数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse函数执行了')
        # print(response.text)
        # 提取招聘信息条目的列表
        job_list = response.xpath('//ul[contains(@class,"mt10")]/li')
        print(f'len:{len(job_list)}')
        for each in job_list:
            # xpath()返回的是节点对象
            # 使用extract() 把节点对象转换成=>unicode字符串
            # 新闻标题
            title =each.xpath('.//a/text()').extract()[0].strip()
            # print(name)
            # 新闻详情链接(拼接完整)
            detail_url = 'http://politics.people.com.cn/'+each.xpath('.//a/@href').extract()[0].strip()
            print('='*50)
            # 使用日志打印
            self.log(f'title:{title}')
            self.log(f'detail_url:{detail_url}')
            # 试试详情 生成请求对象
            req = scrapy.Request(detail_url, callback=self.parse_detail)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        # 翻页处理
        # 方法一
        # next_btn= response.xpath('//div[@class="page_n clearfix"]/a[text()="下一页"]')
        # if next_btn:
        #     next_page_url = next_btn[0].xpath('./@href').extract()[0]
        #     pat = re.compile(r'(index\d+\.html)')
        #     next_page_url = pat.sub(next_page_url,response.url)
        #     print(f'page:{self.page},url:{next_page_url}')
        #
        #     # 生成请求对象
        #     req = scrapy.Request(next_page_url, callback=self.parse)
        #     # 使用yield 把请求对象发送给scheduler,放入请求等待队列
        #     yield req

        self.page += 1
        # 方法二
        if self.page <= self.max_pages:
            url = self.get_url()
            print(f'page:{self.page},url:{url}')
            # 生成请求对象
            req = scrapy.Request(url,callback=self.parse)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req




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
        item = Task2Item()
        item['title']=title
        item['detail_url']=detail_url
        item['detail_text']=detail_text
        item['pub_date']=pub_date
        item['source']=source

        # 把提交给管道pipeline
        yield item
