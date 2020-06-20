# -*- coding: utf-8 -*-
import scrapy

from day13.xtqspider.xtqspider.items import XtqspiderItem

# 直接在首页拿一部分内容
class Xtq1Spider(scrapy.Spider):
    name = 'xtq2'
    allowed_domains = ['zynews.cn']
    start_urls = ['https://xtq.zynews.cn/wzpostlist.php?mod=list']

    def __init__(self):
        self.page = 1
        self.max_pages = 3
        self.str_url = 'https://xtq.zynews.cn/wzpostlist.php?mod=list&page={}'

    def get_url(self):
        return self.str_url.format(self.page)

    def parse(self, response):
        print('parse函数执行了')
        # print(response.text)
        # 提取信息条目的列表
        new_list = response.xpath('//div[@class="bm_c"]/table//tr')
        print(f'len:{len(new_list)}')
        for each in new_list:
            # xpath()返回的是节点对象
            # 使用extract() 把节点对象转换成=>unicode字符串
            # 标题
            item = XtqspiderItem()
            title = each.xpath('.//th[@class="new"]/a/text()').extract()[0].strip()
            item['title'] = title
            # 新闻详情链接(拼接完整)
            detail_url = 'https://xtq.zynews.cn/' + each.xpath('.//th[@class="new"]/a/@href').extract()[0]
            item['detail_url'] = detail_url
            # 发布者
            complainant = each.xpath('.//td[@class="by"]/cite/a/text()').extract()[0].strip()
            item['complainant'] = complainant
            # 发布时间
            pub_date = each.xpath('.//td[@class="by"]/em/span/text()').extract()[0]
            item['pub_date'] = pub_date
            # 使用日志打印
            self.log(f'title:{title}')
            self.log(f'detail_url:{detail_url}')
            self.log(f'complainant:{complainant}')
            self.log(f'pub_date:{pub_date}')
            # 试试详情 生成请求对象  dont_filter=True 不去重
            req = scrapy.Request(detail_url, callback=self.parse_detail, dont_filter=True)
            # 把获取到的数据使用meta，让req携带信息进入yield
            req.meta['item'] = item
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        # 翻页处理
        self.page += 1
        if self.page <= self.max_pages:
            url = self.get_url()
            print(f'page:{self.page},url:{url}')
            # 生成请求对象
            req = scrapy.Request(url, callback=self.parse)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')

        # 提取meta携带的信息
        item = response.meta['item']
        # print(response.url)
        # 获取详情页数据
        detail_text = response.xpath('.//td[@class="t_f"]/text()').extract()
        detail_text = ''.join(detail_text).strip()
        self.log(f'detail_text:{detail_text}')
        # 把详情页提取到的信息补充到item中
        item['detail_text'] = detail_text
        yield item
