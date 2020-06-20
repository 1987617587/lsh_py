# author:lsh
# datetime:2020/4/26 11:44 
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

from selenium import webdriver
from selenium.webdriver.common.by import By  # 元素定位的方式
from selenium.webdriver.support.ui import WebDriverWait  # 等待对象
from selenium.webdriver.support import expected_conditions as EC  # 等待触发条件
import time  # 设置延迟
import codecs  # 打开csv文件
import random  # 生成随机数
import csv  # 操作csv文件，写入操作
import re

# 生成ChromeOptions对象，对selenium做优化，提高爬取效率
opt = webdriver.ChromeOptions()
opt.headless = True # 设置浏览器为无界面浏览器
# 禁止图片加载
prefs = {
    "profile.managed_default_content_settings.images": 2
}
opt.add_experimental_option("prefs", prefs)

url = 'https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c'
# 生成webdriver对象
browser = webdriver.Chrome(chrome_options=opt)  #
# 浏览器窗口最大化
browser.maximize_window()
# 生成等待对象
wait = WebDriverWait(browser, 60)
# 加载京东大药房首页
browser.get(url)
time.sleep(3)
# 获取药品类别的链接
cate_ls = browser.find_elements_by_xpath('//map[@id="Map_m"]//area')
cate_url_ls = []
for each1 in cate_ls:
    cate_url = each1.get_attribute('href')
    cate_url_ls.append(cate_url)
print('cate len:', len(cate_url_ls))
duration = 1
# 获取指定类别下药品类表
for each2 in cate_url_ls:
    cate_url = each2
    print('cate_url:', cate_url)
    page = 1
    while True:
        page_count = 1
        browser.get(cate_url)
        time.sleep(random.random())
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight-800);')
        wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@id="J_goodsList"]/ul/li[@class="gl-item"]//div[@class="p-price"]'))
        )
        # 获取页数
        # page_count = browser.find_elements_by_xpath('//span[@class="p-skip"]/em/b')[0].text
        if page_count == 1:
            page_count = wait.until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="p-skip"]/em/b'))
            )
            page_count = page_count.text.strip()
            page_count = int(page_count)
        print('page_count:', page_count)
        # 获取药品列表
        mls = browser.find_elements_by_xpath('//div[@id="J_goodsList"]/ul/li[@class="gl-item"]')
        print('mls_len:', len(mls))
        # 提取药品详情链接
        medicine_url_ls = []
        for each3 in mls:
            murl = each3.find_elements_by_xpath('.//div[@class="p-img"]/a')[0].get_attribute('href')
            medicine_url_ls.append(murl)
        print('medicine_url_ls_len:', len(medicine_url_ls))

        # 药品详情信息
        for each4 in medicine_url_ls:
            print('medicine_url:', each4)
            browser.get(each4)
            time.sleep(random.random() + duration)
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
                        type = type.replace(',', ' ')

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
            time.sleep(random.random() + duration)

        # 翻页
        page += 1
        if page > page_count:
            break
        else:
            pat = re.compile(r'page=(\d+)')
            next_page_url = pat.sub('page=' + str(page), cate_url)
            print('next_page_url:', next_page_url)
            browser.get(next_page_url)

browser.quit()