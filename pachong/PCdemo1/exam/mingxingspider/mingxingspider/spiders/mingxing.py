# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from exam.mingxingspider.mingxingspider.items import MingxingspiderItem


class MingxingSpider(CrawlSpider):
    name = 'mingxing'
    allowed_domains = ['tvmao.com']
    start_urls = ['https://www.tvmao.com/star']

    # 匹配详情链接
    link_item = LinkExtractor(restrict_xpaths=('//a[contains(@class,"black_link")]'))

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
        if 'star' not in response.url:
            return
        print('parse_detail函数执行了')
        print(response.url)
        # 获取详情页数据
        name = response.xpath('//h1/text()').extract()[0].strip()[0:-2]
        introductions = response.xpath('//table[@class="star_meta"]//td[@class="pd5 wd220"]/text()')
        if introductions:
            if len(introductions) > 0:
                English_name = introductions.extract()[0].strip()
            else:
                English_name = '空'

            if len(introductions) > 1:
                blood_type = introductions.extract()[1].strip()
            else:

                blood_type = '空'

            if len(introductions) > 2:
                country = introductions.extract()[2].strip()
            else:

                country = '空'

            if len(introductions) > 3:
                height = introductions.extract()[3].strip()
            else:

                height = '空'

            if len(introductions) > 4:
                weight = introductions.extract()[4].strip()
            else:

                weight = '空'

            if len(introductions) > 5:
                birthday = introductions.extract()[5].strip()
            else:

                birthday = '空'

            if len(introductions) > 6:
                graduation_school = introductions.extract()[6].strip()
            else:
                English_name = '空'

                graduation_school = '空'
            if len(introductions) > 7:
                birthplace = introductions.extract()[7].strip()
            else:

                birthplace = '空'

            if len(introductions) > 8:
                constellation = introductions.extract()[8].strip()
            else:

                constellation = '空'

        else:
            English_name = '空'
            blood_type = '空'
            height = '空'
            country = '空'
            weight = '空'
            birthday = '空'
            birthplace = '空'
            constellation = '空'
            graduation_school = '空'
        print(name, English_name, blood_type, height, country, weight, birthplace, birthday, constellation,
              graduation_school)

        introduction = response.xpath('//div[@class="lessmore"]/p//text()').extract()[0].strip()
        print(introduction)
        # /html/body/div[4]/div/div[2]
        TV = response.xpath('//div[@class="section-wrap pt10"]/div[2]/ul[@class="work_pics"]/li/a/div[@class="mt5"]/text()').extract()
        # if TV is None:
        #     TV = '空'
        TV = ''.join(TV)
        print(TV)
        film = response.xpath(
            '//div[@class="section-wrap pt10"]/div[3]/ul[@class="work_pics"]/li/a/div[@class="mt5"]/text()').extract()
        # if film is None:
        #     TV = '空'
        film = ''.join(film)
        print(film)

        # 存储
        item = MingxingspiderItem()
        item['name'] = name
        item['English_name'] = English_name
        item['blood_type'] = blood_type
        item['country'] = country
        item['height'] = height
        item['weight'] = weight
        item['birthday'] = birthday
        item['graduation_school'] = graduation_school
        item['birthplace'] = birthplace
        item['constellation'] = constellation
        item['introduction'] = introduction
        item['TV'] = TV
        item['film'] = film
        # 把提交给管道pipeline
        yield item

