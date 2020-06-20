# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs
import xlwt  # excel文档的写操作
import pymysql
from scrapy.exporters import JsonItemExporter


class JobspiderPipeline(object):

    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('51jb.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['职业', '公司', '工作地点', '薪资', '发布时间'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['corp'], item['city'], item['salary'], item['pud_date']])
        return item

    def close_spider(self, spider):
        self.file.close()


# 新建管道
class JobspiderMysqlPipeline(object):
    '''
    实现mysql数据的存储
    '''

    def __init__(self):
        '''
        初始化，建立数据库连接
        '''
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='py1911')
        self.cur = self.conn.cursor()
        print("数据库连接成功")

    def process_item(self, item, spider):
        strsql = 'insert into job51 values(0,%s,%s,%s,%s,%s)'
        params = [item['name'], item['corp'], item['city'], item['salary'], item['pud_date']]
        self.cur.execute(strsql, params)
        self.conn.commit()
        print("存储成功")

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


# 新建管道2
class JobspiderExclePipeline(object):
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
        self.sheet1 = self.xls.add_sheet('51job')
        self.row = 1
        # 添加字段标题'职业','公司','工作地点','薪资','发布时间'
        self.sheet1.write(0, 0, '序号')
        self.sheet1.write(0, 1, '职业')
        self.sheet1.write(0, 2, '公司')
        self.sheet1.write(0, 3, '工作地点')
        self.sheet1.write(0, 4, '薪资')
        self.sheet1.write(0, 5, '发布时间')
        self.sheet1.write(0, 6, '岗位描述')


    def process_item(self, item, spider):
        # item['name'],item['corp'],item['city'],item['salary'],item['pud_date']
        self.sheet1.write(self.row, 0, self.row)
        self.sheet1.write(self.row, 1, item['name'])
        self.sheet1.write(self.row, 2, item['corp'])
        self.sheet1.write(self.row, 3, item['city'])
        self.sheet1.write(self.row, 4, item['salary'])
        self.sheet1.write(self.row, 5, item['pud_date'])
        self.sheet1.write(self.row, 6, item['job_msg'])
        print("存储成功")
        self.row += 1

        return item

    def close_spider(self, spider):
        # 对表格进行保存
        self.xls.save('51job.xls')


# 新建管道2
class JobspiderJsonPipeline(object):
    '''
    json格式数据存储
    '''
    def __init__(self):
        self.file = open('51job.json','wb')
        self.exporter = JsonItemExporter(self.file,ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()