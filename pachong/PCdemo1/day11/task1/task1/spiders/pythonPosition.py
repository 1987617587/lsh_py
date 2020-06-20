# -*- coding: utf-8 -*-
import scrapy

from day11.task1.task1.items import Task1Item


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        # 提取招聘信息条目的列表
        job_list = response.xpath('//div[@class="rank-list-wrap"]/ul[@class="rank-list"]/li[@class="rank-item"]')
        print(f'len:{len(job_list)}')

        for each in job_list:
            # xpath()返回的是节点对象
            # 使用extract() 把节点对象转换成=>unicode字符串
            number = each.xpath('.//div[@class="num"]/text()').extract()[0].strip()
            title = each.xpath('.//div[@class="content"]/div[@class="info"]/a/text()').extract()[0].strip()
            url = each.xpath('.//div[@class="content"]/div[@class="info"]/a/@href').extract()[0].strip()
            score = each.xpath('.//div[@class="content"]//div[@class="pts"]/text()').extract()[0].strip()
            playback_volume = each.xpath('.//div[@class="detail"]/span[1]/text()').extract()[0].strip()
            comments = each.xpath('.//div[@class="detail"]/span[2]/text()').extract()[0].strip()
            author = each.xpath('.//div[@class="detail"]/a/span/text()').extract()[0].strip()
            # print(pud_date)
            print('=' * 50)
            # 使用日志打印
            self.log(f'number:{number}')
            self.log(f'title:{title}')
            self.log(f'url:{url}')
            self.log(f'score:{score}')
            self.log(f'playback_volume:{playback_volume}')
            self.log(f'comments:{comments}')
            self.log(f'author:{author}')
            # 存储
            item = Task1Item()
            item['number'] = number
            item['title'] = title
            item['url'] = url
            item['score'] = score
            item['playback_volume'] = playback_volume
            item['comments'] = comments
            item['author'] = author
            # 把提交给管道pipeline
            yield item

