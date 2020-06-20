from selenium import webdriver
# 导入元素定位方式
from selenium.webdriver.common.by import By
# WebDriverWait,智能等待对象，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件触发
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://ewealth.abchina.com/fund/150010.htm')

# 创建智能等待对象
wait = WebDriverWait(browser, 10)
try:
    # 页面循环等待
    # 等待条件<li id="FundChanged" style="">... </li>下的所有元素加载完毕
    # 达到条件，停止等待
    ls = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//li[@id="FundChanged"]/fonts')))
    for item in ls:
        print(item.text)

    print()
except Exception as e:
    print(e)
finally:
    browser.quit()
