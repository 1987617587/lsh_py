from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# 智能等待对象
wait = WebDriverWait(browser, 60)
url = 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1654'
browser.get(url)
page = 1
while True:
    print('page:', page)
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="pages"]/table/tbody/tr/td[6]/span'))
    )

    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//tr[@class= "evenBj"]/td[2]'), '1654')
    )

    ls = browser.find_elements_by_xpath('//tr[@class="evenBj"]')
    print('len:', len(ls))
    if len(ls) > 0:
        for item in ls:
            tds = item.find_elements_by_xpath('./td')
            num = tds[0].text
            print('序号：', num)
            ann_num = tds[1].text
            print('公告序号：', ann_num)
            ann_date = tds[2].text
            print('公告日期：', ann_date)
            reg_num = tds[4].text
            print('注册号：', reg_num)
            company = tds[5].text
            print('申请人：', company)
            brand = tds[6].text
            print('商标名称：', brand)
            print('=' * 200)

        try:
            time.sleep(1)
            btn_next = browser.find_element_by_xpath('//*[@id="pages"]/table/tbody/tr/td[8]/a')
            btn_next.click()
            page += 1
        except Exception as e:
            print('over..')
            break
time.sleep(3)
browser.close()