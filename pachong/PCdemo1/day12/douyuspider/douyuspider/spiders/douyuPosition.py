# -*- coding: utf-8 -*-
import json

import scrapy

from day12.douyuspider.douyuspider.items import DouyuspiderItem


class DouyupositionSpider(scrapy.Spider):
    name = 'douyuPosition'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        # print(response.text)

        # 返回从 json 里获取 data 段数据集合
        data = json.loads(response.text)["data"]
        for each in data:
            item = DouyuspiderItem()
            item["name"] = each["nickname"]
            item["image_url"] = each["vertical_src"]
            yield item

        if self.offset <= 160:
            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)