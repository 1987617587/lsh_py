# -*- coding: utf-8 -*-
'''
演示自动化爬取
'''
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from day13.xtqspider.xtqspider.items import XtqspiderItem


# 修改父类 CrawlSpider
class Xtq3Spider(CrawlSpider):
    name = 'xtq3'
    allowed_domains = ['zynews.cn']
    start_urls = ['https://xtq.zynews.cn/wzpostlist.php?mod=list']

    # 匹配翻页链接 可以使用re,css,xpath
    # link_page = LinkExtractor(restrict_xpaths=('//a[@class="nxt"]'))
    # link_page = LinkExtractor(restrict_css='a.next')
    # 使用正则不用担心匹配可能会重复，自带去重
    link_page = LinkExtractor(allow=(r'wzpostlist\.php\?mod=list'))
    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//div[@class="bm_c"]//tr/th[@class="new"]/a'))
    # 定义规则
    rules = [
        Rule(link_page, follow=True),
        Rule(link_item, callback='parse_detail',follow=False)
    ]

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
        complainant_list = response.xpath('//div[@id="postlist"]/div/table/tr[1]')
        print(f'complainant_len:{len(complainant_list)}')
        for each in complainant_list:
            complainant = \
            each.xpath('.//a[@class="xw1"]/text()').extract()[0].strip()
            detail_text = each.xpath('.//td[@class="t_f"]/text()').extract()
            detail_text = ''.join(detail_text).strip()
            pub_date = each.xpath('.//td[@class="plc"]//div[@class="pti"]/div[@class="authi"]/em/text()').extract()[
                0].strip()
            self.log(f'title:{title}')
            self.log(f'detail_url:{detail_url}')
            self.log(f'detail_text:{detail_text}')
            self.log(f'complainant:{complainant}')
            self.log(f'pub_date:{pub_date}')
            # 存储
            # item = XtqspiderItem()
            # item['title'] = title
            # item['detail_url'] = detail_url
            # item['detail_text'] = detail_text
            # item['complainant'] = complainant
            # item['pub_date'] = pub_date
            #
            # # 把提交给管道pipeline
            # yield item

