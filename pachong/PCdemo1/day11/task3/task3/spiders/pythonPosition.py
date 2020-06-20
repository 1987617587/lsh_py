# -*- coding: utf-8 -*-
import scrapy

from day11.task3.task3.items import Task3Item
'''
心通桥（spider）
https://xtq.zynews.cn/wzpostlist.php?mod=list
爬去投诉帖子的标题，链接，内容，投诉者，投诉时间
存储到mysql数据库'''

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['xtq.zynews.cn']
    start_urls = ['https://xtq.zynews.cn/wzpostlist.php?mod=list']

    def __init__(self):
        self.page = 1
        self.max_pages = 3
        self.str_url  = 'https://xtq.zynews.cn/wzpostlist.php?mod=list&page={}'

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
        job_list = response.xpath('//div[@class="bm_c"]//tr/th[@class="new"]')
        print(f'len:{len(job_list)}')
        for each in job_list:
            # xpath()返回的是节点对象
            # 使用extract() 把节点对象转换成=>unicode字符串
            # 标题
            title = each.xpath('.//a/text()').extract()[0].strip()
            # 新闻详情链接(拼接完整)
            detail_url = 'https://xtq.zynews.cn/'+each.xpath('.//a/@href').extract()[0].strip()
            print('='*50)
            # 使用日志打印
            self.log(f'title:{title}')
            self.log(f'detail_url:{detail_url}')
            # 试试详情 生成请求对象
            req = scrapy.Request(detail_url, callback=self.parse_detail)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        # 翻页处理
        self.page += 1
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
        title = response.xpath('//a[@id="thread_subject"]/text()').extract()[0].strip()
        detail_url = response.url

        # 提取招聘信息条目的列表
        complainant_list = response.xpath('//div[@id="postlist"]/div/table/tr')
        print(f'complainant_len:{len(complainant_list)}')
        for each in complainant_list:


            complainant = response.xpath('.//td[@class="pls "]/div[@class="pi"]/div[@class="authi"]/a/text()').extract()[0].strip()
            detail_text = response.xpath('.//td[@class="t_f"]/text()').extract()[0].strip()
            pub_date = response.xpath('.//td[@class="plc"]//div[@class="pti"]/div[@class="authi"]/em/text()').extract()[0].strip()
            self.log(f'title:{title}')
            self.log(f'detail_url:{detail_url}')
            self.log(f'detail_text:{detail_text}')
            self.log(f'complainant:{complainant}')
            self.log(f'pub_date:{pub_date}')
            # 存储
            item = Task3Item()
            item['title']=title
            item['detail_url']=detail_url
            item['detail_text']=detail_text
            item['complainant']=complainant
            item['pub_date']=pub_date

            # 把提交给管道pipeline
            yield item
