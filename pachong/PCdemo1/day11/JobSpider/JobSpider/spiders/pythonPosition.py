# -*- coding: utf-8 -*-
import scrapy

from day11.JobSpider.JobSpider.items import JobspiderItem


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition' # 这是爬虫的识别名称，必须位移
    allowed_domains = ['51job.com'] # 搜索的域名范围
    # start_urls = ['http://51job.com/'] # 爬取的url列表
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare'] # 爬取的url列表

    def __init__(self):
        self.city = 100000
        self.max_cities = 40000
        self.page = 1
        self.max_pages = 3
        self.str_url = 'https://search.51job.com/list/0{},000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare'


    def get_url(self):
        return self.str_url.format(self.city,self.page)


    def parse(self, response):
        '''
        进行数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse函数执行了')
        # self.log('url:'+response.url)
        # self.log('status:'+str(response.status))
        # self.log('html:'+response.text)
        # print(response.text)

        # 提取招聘信息条目的列表
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print(f'len:{len(job_list)}')

        for each in job_list:
            # xpath()返回的是节点对象
            name =each.xpath('.//p[@class="t1 "]/span/a/@title')
            name =each.xpath('.//p[@class="t1 "]/span/a/text()')
            # 使用extract() 把节点对象转换成=>unicode字符串
            name =each.xpath('.//p/span/a/text()').extract()[0].strip()
            # print(name)
            # 招聘公司
            corp = each.xpath('.//span[@class="t2"]/a/text()').extract()[0].strip()
            # print(corp)
            # 工作地点
            city =each.xpath('.//span[@class="t3"]/text()').extract()[0].strip()
            # print(city)
            # 薪资待遇(可能为空)
            salary =each.xpath('.//span[@class="t4"]/text()').extract()
            if salary:
                salary = salary[0].strip()
            else:
                salary = '面议'
            # print(salary)
            # 发布时间
            pud_date = each.xpath('.//span[@class="t5"]/text()').extract()[0].strip()
            # print(pud_date)
            print('='*50)
            # 使用日志打印
            self.log(f'name:{name}')
            self.log(f'corp:{corp}')
            self.log(f'city:{city}')
            self.log(f'salary:{salary}')
            self.log(f'pud_date:{pud_date}')
            # 存储
            item = JobspiderItem()
            item['name']=name
            item['corp']=corp
            item['city']=city
            item['salary']=salary
            item['pud_date']=pud_date

            # 试试详情 生成请求对象

            detail_url = each.xpath('.//p/span/a/@href').extract()[0].strip()
            req = scrapy.Request(detail_url, callback=self.parse_detail)
            req.meta['item'] = item
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        # 翻页处理
        self.page += 1
        if self.page <= self.max_pages:
            url = self.get_url()
            print(f'page:{self.page},city:{self.city},url:{url}')
            # 生成请求对象
            req = scrapy.Request(url,callback=self.parse)
            # 使用yield 把请求对象发送给scheduler,放入请求等待队列
            yield req

        else:
            # 开始切换城市
            self.city+=10000
            if self.city <= self.max_cities:
                self.page = 1
                url = self.get_url()
                print(f'page:{self.page},city:{self.city},url:{url}')
                # 生成请求对象
                req = scrapy.Request(url, callback=self.parse)
                # 使用yield 把请求对象发送给scheduler,放入请求等待队列
                yield req



    def parse_detail(self, response):
        '''
        进行详情页数据的提取
        :param response:响应对象，它包含了响应信息
        :return:
        '''
        print('parse_detail函数执行了')
        print(response.url)

        # 职位说明
        job_msg_list = response.xpath('//div[contains(@class,"job_msg")]/p')
        print(f'len:{len(job_msg_list)}')
        str_msg = ''
        for job_msg in job_msg_list:
            job_msg = job_msg.xpath('./text()')
            if job_msg:
                job_msg = job_msg.extract()[0].strip()
                print(f'job_msg:{job_msg}')
                str_msg +=job_msg

        item = response.meta['item']
        item['job_msg'] = str_msg
        # 把提交给管道pipeline
        yield item

