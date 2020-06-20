# author:lsh
# datetime:2020/4/17 14:32 
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
import os

import requests
import re
import pytesseract
from selenium import webdriver
from PIL import Image
from fontTools.ttLib import TTFont


#
# url = 'https://maoyan.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# html = response.text
# print(html)


class NumberParser:
    def __init__(self):
        '''
        初始化
        '''
        self.content = None
        self.url = None
        self.names = []
        self.chars = []
        self.font_dict = {}

    def get_headers(self):
        '''
        获取请求头
        :return:
        '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }
        return headers

    def downpage(self, url):
        '''
        下载指定页面
        :return:
        '''
        response = requests.get(url, headers=self.get_headers())
        self.content = response.text
        self.url = url

    def fontHandler0(self):
        '''
        解析字体的链接，下载字体,此处演示本地的一个字体
        :return:
        '''
        font = TTFont('fonts/maoyan.woff')
        # 获取字体文件中可显示字体名称，转换成显示内容
        self.names = font.getGlyphNames()
        # print(self.names)
        self.chars = []
        tmps = []
        for name in self.names:
            if name.find('uni') >= 0:
                char = name.replace('uni', '&#x') + ';'
                tmps.append(name)
                self.chars.append(char)
        self.names = tmps
        print(self.names)
        print(self.chars)  # 自定义字体可显示的字符

    def fontHandler(self):
        '''
        解析字体的链接，下载字体
        :return:
        '''
        # 根据上个操作，不在加载本地字体，直接去网页下载
        # font = TTFont('fonts/maoyan.woff')
        pat_font_url = re.compile(r"\n           url\('(//.*?woff)'\)", re.S)
        font_url = pat_font_url.search(self.content)
        print(font_url)
        font_url = 'http:' + font_url.group(1).strip()
        print(font_url)
        # 下载字体
        ttf = requests.get(font_url, stream=True, headers=self.get_headers())
        with open('fonts/maoyan.woff', 'wb')as file:
            for chunk in ttf.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        # 对下载好的字体进行读取
        self.font = TTFont('fonts/maoyan.woff')

    def getHtml(self):
        '''
        生成html文件（利用我们的模板，把加密的字符添加到span标签中）

        :return:
        '''
        # 获取字体文件中可显示字体名称，转换成显示内容
        self.names = self.font.getGlyphNames()
        # print(self.names)
        self.chars = []
        tmps = []
        for name in self.names:
            if name.find('uni') >= 0:
                char = name.replace('uni', '&#x') + ';'
                tmps.append(name)
                self.chars.append(char)
        self.names = tmps
        print(self.names)
        print(self.chars)  # 自定义字体可显示的字符

        # 打开定义好的模板html文件
        with open('html/font_template.html', 'r', encoding='utf-8')as file:
            html = file.read()
        # 匹配模板html中的span标签    <span class="stonefont"> </span>
        pat1 = re.compile(r'<span class="stonefont">(.*?)</span>', re.S)
        html = pat1.sub('<span class="stonefont">' + '&nbsp;'.join(self.chars) + '</span>', html)
        with open('html/font.html', 'w', encoding='utf-8')as file:
            file.write(html)

    def parseFont(self):
        '''
        使用下载的字体进行解密，进行文字识别，解析文字文件中能显示的字符
        然后截图，建立我们自己的解码字典
        :return:
        '''
        # options = webdriver.ChromeOptions()

        browser = webdriver.Chrome()

        browser.get('file:///' + os.path.abspath('html/font.html'))
        browser.save_screenshot('images/demo01.png')
        img = Image.open('images/demo01.png')
        # 获取解码后的数字
        text = pytesseract.image_to_string(img).replace(' ', '')
        print(text)
        # 建立映射（解码）
        self.font_dict = {self.names[i]: text[i] for i in range(len(self.names))}
        self.font_dict2 = {self.chars[i]: text[i] for i in range(len(self.names))}
        # 获取到我们的解码字典
        print(self.font_dict)
        print(self.font_dict2)
        browser.close()

    def convert_num(self, val):
        '''
        根据数字，进行转换 &#xee57; ==》uniEE57
        :param val:
        :return:
        '''
    #     此处直接paresNumbers（）解码时使用

    def paresNumbers(self, val):
        '''
        遍历解密网页中加密数字字符串
        :param val:
        :return:
        '''
        # 遍历字典
        for key, value in self.font_dict2.items():
            key = '&#x' + key[3:-1].lower() + ';'
            # print(key)
            if key in val:
                val = val.replace(key, value)
        print('val:', val)
        print('=' * 22)

    def parse(self):
        '''
        解析网页
        :return:
        '''
        pat1 = re.compile(r'<ul class="ranking-wrapper ranking-box">(.*?)</ul>', re.M | re.S)
        match_obj = pat1.search(self.content)
        content = match_obj.group(1)
        pat2 = re.compile(r'<li.*?>(.*?)</li>', re.M | re.S)
        ls = pat2.findall(content)
        print('len：', len(ls))
        for each in ls:
            pat3 = re.compile(r'<span class="stonefont">(.*?)</span>', re.M | re.S)
            ranking_nums = pat3.search(each).group(1)
            print('ranking_nums:', ranking_nums)
            # 遍历字典
            for key,value in self.font_dict2.items():
                key = '&#x'+key[3:-1].lower()+';'
                # print(key)
                if key in ranking_nums:
                    ranking_nums = ranking_nums.replace(key,value)
            print('ranking_nums:', ranking_nums)
            print('='*22)



if __name__ == '__main__':
    parse = NumberParser()
    url = 'https://maoyan.com/'
    parse.downpage(url)
    parse.fontHandler()
    parse.getHtml()
    parse.parseFont()
    parse.parse()
    # parse.convert_num(1)
