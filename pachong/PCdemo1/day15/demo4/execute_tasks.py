# author:lsh
# datetime:2020/4/13 15:35 
"""
                                 .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
"""
import requests
from lxml import etree
from weather_work import crawl


class Clinet:
    def __init__(self):
        self.urls = []
        self.base_url = 'https://www.tianqi.com'

    def get_urls(self):
        url = 'https://www.tianqi.com/chinacity.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }
        # 请求城市列表，提取城市天气链接
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.content)
        ls = html.xpath('//div[@class="citybox"]/span//a')
        for item in ls:
            city = item.xpath('./text()')[0]
            city_url = self.base_url + item.xpath('./@href')[0]
            print(city, city_url)
            self.urls.append((city, city_url))

    def task_manage(self):
        '''
        把任务添加到任务队列中
        :return:
        '''
        for item in self.urls:
            crawl.delay(item[0], item[1])


if __name__ == '__main__':
    client = Clinet()
    client.get_urls()
    client.task_manage()
