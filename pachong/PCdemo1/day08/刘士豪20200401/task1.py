'''

案例：中国商标网公告爬虫（selenium）
http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/homePage.html
http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1654
爬取期号为1654的公告信息：序号，期号，公告日期，注册号，申请人，商标名称

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re

browser = webdriver.Chrome()
browser.maximize_window()
# 定义等待条件
wait = WebDriverWait(browser, 60)
try:
    browser.get('http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/homePage.html')
    # 输入框
    tb_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#annNum'))
    )
    # 按钮
    search_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#annNumSubmit'))
    )
    tb_input.clear()
    tb_input.send_keys('1654')
    time.sleep(3)

    search_btn.click()
    # 等待搜索结果中的条目加载完成
    wait.until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, '.jsTj.w1008'))
        EC.presence_of_element_located((By.CSS_SELECTOR, '.searchAnnnum'))
    )
    # 等待加载页数元素
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#pages'))
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
        print(f"正在加载第{page}页")
        # 等待搜索结果中的条目加载完成
        wait.until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, '.jsTj.w1008'))
            EC.presence_of_element_located((By.CSS_SELECTOR, '.searchAnnnum'))
        )
        ls = browser.find_elements_by_xpath('//tr[@class="evenBj"]')
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random())
        print(f'len:{len(ls)}')
        for item in ls:
            print(item.text)

            serial_number = item.find_element_by_xpath('.//td[1]').text.strip()
            print(f'serial_number:{serial_number}')
            lssue_number = item.find_element_by_xpath('.//td[2]/a').text.strip()
            print(f'lssue_number:{lssue_number}')
            announcement_date = item.find_element_by_xpath('.//td[3]').text.strip()
            print(f'announcement_date:{announcement_date}')
            # registration_number, applicant, trade_name
            registration_number = item.find_element_by_xpath('.//td[5]').text.strip()
            print(f'registration_number:{registration_number}')
            applicant = item.find_element_by_xpath('.//td[6]').text.strip()
            print(f'applicant:{applicant}')
            trade_name = item.find_element_by_xpath('.//td[7]').text.strip()
            print(f'trade_name:{trade_name}')
            print('=' * 99)
        # 翻页
        if page <= total:
            page += 1
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')
            btn_next = browser.find_element_by_xpath('//*[@id="pages"]/table/tbody/tr/td[8]/a')

            print('next page ...')
            # 移动鼠标去点击下一页
            # ActionChains(browser).move_to_element(next_page_btn).click().perform()
            btn_next.click()
            time.sleep(3)
        else:
            break

    time.sleep(random.random())

except Exception as e:
    print(e)
finally:
    browser.quit()
