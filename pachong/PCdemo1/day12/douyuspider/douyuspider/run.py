'''
用于启动爬虫项目
'''
from scrapy import cmdline
name ='douyuPosition'
cdm ='scrapy crawl {0}'.format(name)

if __name__ == '__main__':
    # cmdline.execute()内参数需要是列表，使用切割空格，生成列表
    cmdline.execute(cdm.split())
