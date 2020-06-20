'''

案例：京东大药房爬虫
https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c
爬取标题，价格，品牌，商品名称，类别，适用症状，适用类型
保存到csv文件
'''
import codecs
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
# 禁止图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)
# 无界面浏览器
# options.add_argument('--headless')
# 添加 UA
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"')
browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.Chrome()
browser.maximize_window()
# 定义等待条件
wait = WebDriverWait(browser, 60)
# try:
browser.get(
    'https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c')

# 等待搜索结果中的商品类别加载完成
# wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, '#Map_m'))
# )

ls = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="Map_m"]/area'))
)
time.sleep(random.random())
print(f'len:{len(ls)}')
for item in ls:
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Map_m"]/area'))
    )

    category_url = item.get_attribute('href')
    print(f'category_url:{category_url}')
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
    # while True:
    #
    #     goods = browser.find_elements_by_xpath('//li[@class="gl-item"]')
    #     browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    #     time.sleep(random.random())
    #     print(f'本页商品数:{len(goods)}')
    #     for good in goods:
    #
    #         time.sleep(random.random())
    #         detail_url = good.find_element_by_xpath('.//div[@class="p-img"]/a').get_attribute('href')
    #         print(f'detail_url:{detail_url}')
    #
    #         # 进入详情页
    #
    #         detail_btn = good.find_element_by_xpath('.//div[@class="p-img"]/a')
    #         detail_btn.click()
    #
    #
    #
    #
    #         all_handles = browser.window_handles
    #         # print(all_handles)
    #         #
    #         time.sleep(2+random.random())
    #         # wait.until(
    #         #     EC.presence_of_all_elements_located((By.XPATH, '//div[@class="summary-price-wrap"]'))
    #         # )
    #         title = browser.find_element_by_xpath('//div[@class="sku-name"]').text.strip()
    #         print(f'title:{title}')
    #
    #         # price = good.find_element_by_xpath(
    #         #     '//div[@class="dd"]/span[@class="p-price"]/span[2]').text.strip()
    #         # print(f'price:{price}')
    #         #
    #         # comment_nums = good.find_element_by_xpath('//div[@id="comment-count"]/a').text.strip()
    #         # print(f'comment_nums:{comment_nums}')
    #         #
    #         # brand = good.find_element_by_xpath('//ul[@id="parameter-brand"]/li').get_attribute('title')
    #         # print(f'brand:{brand}')
    #         #
    #         # name = good.find_element_by_xpath('//ul[@class="parameter2 p-parameter-list"]/li[1]').get_attribute(
    #         #     'title')
    #         # print(f'name:{name}')
    #         #
    #         # applicable_symptom = good.find_element_by_xpath(
    #         #     '//ul[@class="parameter2 p-parameter-list"]/li[8]').get_attribute(
    #         #     'title')
    #         # print(f'applicable_symptom:{applicable_symptom}')
    #         #
    #         # applicable_type = good.find_element_by_xpath(
    #         #     '//ul[@class="parameter2 p-parameter-list"]/li[10]').get_attribute(
    #         #     'title')
    #         # print(f'applicable_type:{applicable_type}')
    #         # # 数据存储
    #         # # .csv格式codecs. 在打开文件时避免空行，用open会有空行
    #         # with codecs.open('jd.csv', 'a', encoding='utf-8') as file:
    #         #     wr = csv.writer(file)  # 对csv操作，需要生成csv的writer对象
    #         #     wr.writerow([title, detail_url, price, comment_nums,brand,name,applicable_symptom,applicable_type])
    #
    #         # time.sleep(random.random())
    #
    #         print('--')
    #         time.sleep(random.random())
    #         print(len(all_handles))
    #
    #         # browser.switch_to_window(all_handles[1])
    #         # browser.close()
    #
    #
    #     # 翻页
    #     if page <= total:
    #         page += 1
    #         browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')
    #
    #         next_page_btn = browser.find_element_by_xpath( '//a[@class="pn-next"]')
    #         print('next page ...')
    #         # 移动鼠标去点击下一页
    #         ActionChains(browser).move_to_element(next_page_btn).click().perform()
    #     else:
    #         break
    browser.back()
    time.sleep(random.random())
    print('=' * 99)
time.sleep(random.random())
# except Exception as e:
#     print(e)
# finally:
#     browser.quit()
