from selenium import webdriver
# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://www.taobao.com/')

### 单个元素查找
input_1 = browser.find_element_by_id('q')
input_2 = browser.find_element_by_xpath('//*[@id="q"]')
input_3 = browser.find_element_by_css_selector('#q')
input_4 = browser.find_element_by_class_name('search-combobox-input')

print(input_1)
print(input_2)
print(input_3)
print(input_4)
#
# find_element_by_name
# find_element_by_id
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
### 多个元素查找
# find_elements_by_name
# find_elements_by_id
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector