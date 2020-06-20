from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.baidu.com'
browser.get(url)
# 截屏
browser.save_screenshot('./images/img_1.png')
browser.close()