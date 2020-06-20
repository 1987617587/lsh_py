# -*- coding: utf-8 -*-
import scrapy

from day12.xietiandispider.xietiandispider.items import XietiandispiderItem


class XietiandiSpider(scrapy.Spider):
    name = 'xietiandi'
    allowed_domains = ['xietd.com']
    start_urls = ['http://www.xietd.com/portal.php?&page=1#tab_anchor']
    offset = 1
    def parse(self, response):
        print(f"page:{self.offset}")


        # http://www.xietd.com/portal.php?&page=5#tab_anchor
        # print(response.text)
        ls = response.xpath('//div[@class="work-list-box"]/div[@class="card-box"]')
        print(f'len:{len(ls)}')

        for each in ls:
            detail_url = each.xpath('.//div[@class="card-img"]/a/@href').extract()[0].strip()
            # print(f'detail_url:{detail_url}')
            req = scrapy.Request(detail_url, callback=self.parse_detail)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        if self.offset <= 3:
            self.offset += 1
            next_page_url = 'http://www.xietd.com/portal.php?&page='+str(self.offset)+'#tab_anchor'
            yield scrapy.Request(next_page_url, callback=self.parse)
    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        # print(response.text)
        # 无法获取图片链接src="static/image/common/none.gif"
        print(response.url)

        # 标题
        title = response.xpath('//h2/text()').extract()[0].strip()
        print(f'title:{title}')

        # 图片地址
        image_url_list = response.xpath('//div[@class="aimg"]/img/@zoomfile')
        print(f'image_url_list:{len(image_url_list)}')
        for image_url in image_url_list:
            image_url = 'http://www.xietd.com/'+image_url.extract()
            print(f'image_url:{image_url}')
            item = XietiandispiderItem()
            item['name']=title
            item['image_url'] = image_url
            # 把提交给管道pipeline
            yield item
