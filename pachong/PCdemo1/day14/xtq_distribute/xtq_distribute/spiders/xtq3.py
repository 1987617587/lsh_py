# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from day14.xtq_distribute.xtq_distribute.items import XtqDistributeItem


class Xtq3Spider(RedisCrawlSpider):
    name = 'xtq3'
    redis_key = 'xtq3:start_urls'
    link_page = LinkExtractor(allow=(r'wzpostlist\.php\?mod=list'))
    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//div[@class="bm_c"]//tr/th[@class="new"]/a'))
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
        super(Xtq3Spider, self).__init__(*args, **kwargs)

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
            item = XtqDistributeItem()
            item['title'] = title
            item['detail_url'] = detail_url
            item['detail_text'] = detail_text
            item['complainant'] = complainant
            item['pub_date'] = pub_date

            # 把提交给管道pipeline
            yield item
