# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):

    name = 'renren3'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/966745694/profile']
    strcookies = ''
    # 字典推导式,把strcookies转换成字典
    cookies = {item.split('=')[0]: item.split('=')[1] for item in strcookies.split(';')}

    # 可以重写 Spider 类的 start_requests 方法，附带 Cookie 值，发送 POST 请求
    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)

    # 处理响应内容
    def parse_page(self, response):

        print("===========" + response.url)
        with open("deng.html", "w", encoding='utf-8') as file:
            file.write(response.text)
