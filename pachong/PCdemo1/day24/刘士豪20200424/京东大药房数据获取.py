'''

案例：京东大药房爬虫
https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c
爬取标题，价格，品牌，商品名称，类别，适用症状，适用类型
保存到csv文件
'''
import codecs
import csv

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By # 元素定位方式
from selenium.webdriver.support.ui import WebDriverWait # 等待对象
from selenium.webdriver.support import expected_conditions as EC # 等待触发条件
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
    url = 'https://item.yiyaojd.com/'+url_num+'.html?_='+str(int(time.time()))

    response = requests.get(url,headers=headers)
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
# options.add_argument('--headless')
# 添加 UA
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"')
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
    print(f'category_url:{category_url}')
    category_url_ls.append(category_url)

    # 点击进入分类
    # item.click()
    browser.get(category_url)

    # 等待搜索结果中的商品类别加载完成
    wait.until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-i-wrap.j-sku-item'))
        EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-item'))
    )
    # 等待加载页数元素
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage'))
    )
    total = total.text.strip()
    pat = re.compile(r'(\d+)')
    match_obj = pat.search(total)
    if match_obj:
        total = int(match_obj.group(1))
    else:
        total = 1
    print(f'total:{total}')
    page = 1
    while True:

        goods = browser.find_elements_by_xpath('//li[@class="gl-item"]')
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random())
        print(f'本页商品数:{len(goods)}')
        for good in goods:

            time.sleep(random.random())
            detail_url = good.find_element_by_xpath('.//div[@class="p-name p-name-type-3"]/a').get_attribute('href')
            print(f'detail_url:{detail_url}')
            get_detail(detail_url)




        # 翻页
        if page <= total:
            page += 1
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')

            next_page_btn = browser.find_element_by_xpath( '//a[@class="pn-next"]')
            print('next page ...')
            # 移动鼠标去点击下一页
            ActionChains(browser).move_to_element(next_page_btn).click().perform()
        else:
            break
    browser.back()
    time.sleep(random.random())
    print('=' * 99)
time.sleep(random.random())
# except Exception as e:
#     print(e)
# finally:
#     browser.quit()



