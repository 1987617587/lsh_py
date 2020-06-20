import time

from selenium import webdriver

# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://www.taobao.com/')

# 多个元素查找
# find_elements_by_name
# find_elements_by_id
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

ls = browser.find_elements_by_css_selector('.service-bd li')
print(len(ls))
ls = browser.find_elements_by_tag_name('li')
print(len(ls))
ls = browser.find_elements_by_class_name('service-bd')
print(len(ls))
ls = browser.find_elements_by_xpath('//ul[@class="service-bd"]/li')
print(len(ls))

ls = browser.find_elements_by_link_text('保健品')
print(len(ls))
ls = browser.find_elements_by_partial_link_text('保健')
print(len(ls))
time.sleep(3)



# 关闭当前页面，如果只有一个页面，会关闭浏览器
browser.close()
# 关闭浏览器
browser.quit()