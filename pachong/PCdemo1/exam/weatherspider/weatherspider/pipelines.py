# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import xlwt


class WeatherspiderPipeline(object):
    '''
    实现Excle数据的存储
    '''

    def __init__(self):
        '''
        初始化，添加表头
        '''
        # 生成workbook 对象  execl文档的对象
        self.xls = xlwt.Workbook()
        # 新建execl文档中的sheet
        self.sheet1 = self.xls.add_sheet('weather')
        self.row = 1
        # 添加 省份、城市、天气情况、最高气温、最低气温、日期
        self.sheet1.write(0, 0, '序号')
        self.sheet1.write(0, 1, '省份')
        self.sheet1.write(0, 2, '城市')
        self.sheet1.write(0, 3, '天气情况')
        self.sheet1.write(0, 4, '最高气温')
        self.sheet1.write(0, 5, '最低气温')
        self.sheet1.write(0, 6, '日期')



    def process_item(self, item, spider):
        # [item['province'], item['city'], item['weather'], item['max_temperature'], item['min_temperature'],item['pub_date']]
        self.sheet1.write(self.row, 0, self.row)
        self.sheet1.write(self.row, 1, item['province'])
        self.sheet1.write(self.row, 2, item['city'])
        self.sheet1.write(self.row, 3, item['weather'])
        self.sheet1.write(self.row, 4, item['max_temperature'])
        self.sheet1.write(self.row, 5, item['min_temperature'])
        self.sheet1.write(self.row, 6, item['pub_date'])
        # 支持爬取手动终止
        self.xls.save('weather.xls')
        print("存储成功")
        self.row += 1

        return item

    def close_spider(self, spider):
        # 对表格进行保存
        self.xls.save('weather.xls')

