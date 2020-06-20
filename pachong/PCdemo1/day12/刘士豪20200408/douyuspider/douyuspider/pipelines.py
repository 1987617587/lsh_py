# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
# 导入用于图片下载的管道
from scrapy.pipelines.images import ImagesPipeline
# 导入工具可以获取项目设置中的参数
from scrapy.utils.project import get_project_settings
# 修改父类object =》ImagesPipeline
class DouyuspiderPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
#     #     return item
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        # 当spider中yield提交一个item时，会触发该方法
        print('get_media_requests执行了')
        image_url = item["image_url"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 当s图片下载完成时，会触发该方法
        print(f'results:{results}')
        # 固定写法，获取图片路径，同时判断这个路径是否正确，
        # 如果正确，就放到 image_path 里，ImagesPipeline 源码剖析可见
        print('item_completed:', info)
        if results[0][0] == True:
            image_path = results[0][1]["path"]
            print("2:", image_path)
            # 对图片进行改名
            os.rename(self.IMAGES_STORE + "/" + image_path, self.IMAGES_STORE + "/" +
                      item["name"] + ".jpg")
            item["image_path"] = self.IMAGES_STORE + "/" + item["name"+ ".jpg"]
            return item
