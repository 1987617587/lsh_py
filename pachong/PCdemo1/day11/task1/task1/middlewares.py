# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import hashlib
import time

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse

class Task1SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Task1DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from fake_useragent import UserAgent


class UserAgentMiddleware(object):
    '''
    随机获取ua
    '''

    def __init__(self, user_agent=''):
        self.ua = UserAgent(verify_ssl=False)

    def process_request(self, request, spider):
        print('===UserAgentMiddleware process_request==')
        if self.ua:
            # 显示当前使用的 useragent
            print("********Current UserAgent:%s************")
            print(self.ua.random)
            request.headers.setdefault('User-Agent', self.ua.random)


class WebDriverMiddleware(object):
    '''
    实现scrapy 和 selenium对接，实现动态页面的爬取
    '''

    @classmethod
    def from_crawler(cls, crawler):

        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        # 加载驱动
        print('================process_request================')
        # 无页面
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        browser = webdriver.Chrome(chrome_options=options)
        browser.get(request.url)  # 加载网页
        data = browser.page_source  # 获取网页文本
        data = data.encode('utf-8')
        browser.quit()
        # 封装响应对象
        return HtmlResponse(request.url, body=data, encoding='utf-8', request=request)

    def process_response(self, request, response, spider):

        return response

    def process_exception(self, request, exception, spider):

        pass

    def spider_opened(self, spider):

        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyIPMiddleware(object):
    '''
    scrapy使用讯代理进行动态转发

    '''
    def __init__(self):
        self.orderno = "ZF201910273585ew6xSN"
        self.secret = "1219111fc423464f9f1d3fde3ae6856a"
        self.ip = "forward.xdaili.cn"
        self.port = "80"

    def process_request(self, request, spider):
        print('=======ProxyIPMiddleware=========')
        # 获取请求IP的协议类型（http/https）
        protocal = request.url.split(':')[0]
        print(f'protocal:{protocal}')
        ip_port = self.ip + ":" + self.port
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}

        timestamp = str(int(time.time()))  # 时间戳
        string = ""
        string = "orderno=" + self.orderno + "," + "secret=" + self.secret + "," + "timestamp=" + timestamp
        md5_string = hashlib.md5(string.encode()).hexdigest()  # md5哈希，得到固定长度的字符
        sign = md5_string.upper()  # 转大写字母
        # 构成认证信息
        auth = "sign=" + sign + "&" + "orderno=" + self.orderno + "&" + "timestamp=" + timestamp
        print(f'auth:{auth}')
        # 请求头中设置代理认证的账户密码信息
        request.headers['Proxy-Authorization'] = auth
        # proxy[protocal]根据协议类型获取proxy的值
        request.meta['proxy'] = proxy[protocal]


