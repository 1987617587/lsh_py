from celery import Celery
import requests
from lxml import etree
uri1 = 'redis://@127.0.0.1:6379/3' # 存储执行的结果
uri2 = 'redis://@127.0.0.1:6379/4' # 存储任务队列
app = Celery('weather_work',backend=uri1,broker=uri2)

@app.task
def crawl(loaction,url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    # 请求指定城市的链接，提取天气的信息
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.content)
    temperature = html.xpath('//p[@class="now"]/b/text()')[0]+'℃'
    print(f'{loaction}今天气温{temperature}，链接{url}')
    return [loaction,temperature]







