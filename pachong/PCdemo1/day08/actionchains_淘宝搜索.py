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
    browser.get('https://taobao.com')
    # 输入框
    tb_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )
    # 按钮
    search_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-search.tb-bg'))
    )
    tb_input.clear()
    tb_input.send_keys('移动硬盘')

    search_btn.click()
    # 此处需要先登录 TODO
    # 等待搜索结果中的商品条目加载完成
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist'))
    )
    # 等待加载页数元素
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.total'))
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
        ls = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"item J_MouserOnverReq")]'))
        )
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random())
        print(f'len:{len}')
        for item in ls:
            title = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text.strip()
            print(f'title:{title}')
            detail_url = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').get_attribute('href')
            print(f'detail_url:{detail_url}')
            price = item.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text.strip()
            print(f'price:{price}')
            shop = item.find_element_by_xpath(
                './/a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]').text.strip()
            print(f'shop:{shop}')
            location = item.find_element_by_xpath('.//div[@class="location"]').text.strip()
            print(f'location:{location}')
            nums = item.find_element_by_xpath('.//div[@class="deal - cnt"]').text.strip()
            print(f'nums:{nums}')
            img = item.find_element_by_xpath('.//div[@class="J_ItemPic img"]').get_attribute('src')
            print(f'img:{img}')
            print('=' * 99)

        # 翻页
        if page <= total:
            page += 1
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')
            next_page_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="J_Ajax num icon-tag"]'))
            )
            print('next page ...')
            # 移动鼠标去点击下一页
            ActionChains(browser).move_to_element(next_page_btn).click().perform()
        else:
            break

        time.sleep(random.random())




except Exception as e:
    print(e)
finally:
    browser.quit()
