# author:lsh
# datetime:2020/4/26 9:13 
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
import codecs
import csv

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  # 元素定位方式
from selenium.webdriver.support.ui import WebDriverWait  # 等待对象
from selenium.webdriver.support import expected_conditions as EC  # 等待触发条件
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re
from selenium.webdriver import ChromeOptions
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def get_detail(url):
    pat1 = re.compile(r'(\d+)')
    print(pat1.search(url)[0])
    url_num = pat1.search(url)[0]
    url = 'https://item.yiyaojd.com/' + url_num + '.html?_=' + str(int(time.time()))

    response = requests.get(url, headers=headers)
    print(response.text)
    # pat_price = re.compile(r'(￥\d+)')
    # print(pat_price.search(response.text)[0])

    html = etree.HTML(response.text)
    ls = html.xpath('//ul[@class="parameter2 p-parameter-list"]/li')
    # for each in ls:
    #     print(each.xpath('.//text()')[0])
    # 标题，价格，品牌，商品名称，类别，适用症状，适用类型
    # span_price = html.xpath('//span[@class="p-price"]')[0].text()
    # print(span_price)

    # title = ls[0].xpath('./text()')[0]
    # title = ls[0].xpath('./@title')[0]
    # print(f'title:{title}')
    #
    # price = ls[1].xpath('./@title')[0]
    # print(f'price:{price}')
    #
    # comment_nums = ls[0].xpath('./@title')[0]
    # print(f'comment_nums:{comment_nums}')
    #
    # brand = ls[0].xpath('./@title')[0]
    # print(f'brand:{brand}')

    name = ls[0].xpath('./@title')[0]
    print(f'name:{name}')
    category = ls[8].xpath('./@title')[0]
    print(f'_type:{category}')

    applicable_symptom = ls[5].xpath('./@title')[0]
    print(f'applicable_symptom:{applicable_symptom}')

    applicable_type = ls[8].xpath('./@title')[0]
    print(f'applicable_type:{applicable_type}')
    # # 数据存储
    # # .csv格式codecs. 在打开文件时避免空行，用open会有空行
    # with codecs.open('jd.csv', 'a', encoding='utf-8') as file:
    #     wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
    #     wr.writerow([title, detail_url, price, comment_nums,brand,name,applicable_symptom,applicable_type])

    time.sleep(random.random())
    #


# 生成ChromeOptions对象，对selenium进行优化，提高爬取效率
options = ChromeOptions()
# 禁止图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)
# 无界面浏览器
# options.headless = True
options.add_argument('--headless')
# 添加 UA
options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"')
# 生成浏览器对象
browser = webdriver.Chrome(chrome_options=options)
# browser = webdriver.Chrome()
# 浏览器窗口最大化
browser.maximize_window()
# 定义等待条件
wait = WebDriverWait(browser, 60)
# try:
browser.get(
    'https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c')

# 获取商品类别列表
category_url_ls = []
# 等待搜索结果中的商品类别加载完成
ls = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="Map_m"]/area'))
)
time.sleep(random.random())
print(f'len:{len(ls)}')
for item in ls:
    category_url = item.get_attribute('href')
    # print(f'category_url:{category_url}')
    category_url_ls.append(category_url)
print(category_url_ls)
#
duration = 1
for category_url in category_url_ls:
    print(f'category_url:{category_url}')
    page = 1
    # 进入分类
    while True:

        browser.get(category_url)
        time.sleep(random.random()+duration)
        # 页面垂直滚动
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')

        # 等待搜索结果中的商品价格加载完成
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.p-price'))
        )

        # 获取当前分类的总页数
        page_count = browser.find_element_by_xpath('//span[@class="p-skip"]/em/b').text
        print(f'page_count:{page_count}')
        goods_url_ls = []
        # 当前页的商品列表
        goods = browser.find_elements_by_xpath('//li[@class="gl-item"]')
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random())
        print(f'本页商品数:{len(goods)}')
        for good in goods:
            time.sleep(random.random())
            detail_url = good.find_element_by_xpath('.//div[@class="p-name p-name-type-3"]/a').get_attribute('href')
            # print(f'detail_url:{detail_url}')
            goods_url_ls.append(detail_url)

        # 药品详情信息
        for good_url in goods_url_ls:
            print(f'good_url:{good_url}')
            browser.get(good_url)
            time.sleep(random.random()+duration)

            cate_name = browser.find_elements_by_xpath('//div[@class="crumb fl clearfix"]/div[@class="item"]')
            if len(cate_name) > 1:
                cate_name = cate_name[1].text
            else:
                cate_name = '空'
            print('cate_name:', cate_name)
            medicine_name = browser.find_elements_by_xpath('//div[@class="sku-name"]')[0].text.strip()
            print('medicine_name:', medicine_name)
            price = browser.find_elements_by_xpath(
                '//div[@class="summary-price J-summary-price"]//span[@class="p-price"]/span[contains(@class,"price")]')[
                0].text.strip()
            print('price:', price)
            comm_nums = browser.find_elements_by_xpath('//div[@id="comment-count"]/a')
            if len(comm_nums) > 0:
                comm_nums = comm_nums[0].text.strip()
                if comm_nums[-1] == '+':
                    comm_nums = comm_nums[0:-1]
                unit = comm_nums[-1]
                if unit == '万':
                    comm_nums = comm_nums[0:-1]
                    comm_nums = int(float(comm_nums) * 10000)
                else:
                    comm_nums = int(comm_nums)
            else:
                comm_nums = 0
            print('comm_nums:', comm_nums)
            # 品牌
            brand = browser.find_elements_by_xpath('//ul[@id="parameter-brand"]/li/a')
            if len(brand) > 0:
                brand = brand[0].text.strip()
            else:
                brand = '空'
            print('brand:', brand)
            tmp_ls = browser.find_elements_by_xpath('//ul[@class="parameter2 p-parameter-list"]/li')
            name = '空'
            symptoms = '空'
            type = '空'
            if len(tmp_ls) > 0:
                for elem in tmp_ls:
                    txt = elem.text.strip()
                    tl = txt.split('：')
                    if len(tl) >= 2 and tl[0].find('商品名称') >= 0:
                        name = tl[-1]
                    elif len(tl) >= 2 and tl[0].find('适用症状') >= 0:
                        symptoms = tl[-1]
                    elif len(tl) >= 2 and tl[0].find('适用类型') >= 0:
                        type = tl[-1]
                        type = type.replace(',', ';')

            # 药品名称
            # name =

            print('name:', name)
            print('symptoms:', symptoms)
            print('type:', type)
            print('=' * 200)
            # 数据存储
            filename = 'medicine_data_1911.csv'
            with codecs.open(filename, 'a', encoding='utf-8') as file:
                wr = csv.writer(file)
                wr.writerow([cate_name, medicine_name, price, comm_nums, name, brand, symptoms, type])
            time.sleep(random.random() * duration)
        # 翻页
        page += 1
        if page > page_count:
            break
        else:
            pat = re.compile(r'page=(\d+)')
            next_page_url = pat.sub('page=' + str(page), category_url)
            print('next_page_url:', next_page_url)
            browser.get(next_page_url)

browser.quit()