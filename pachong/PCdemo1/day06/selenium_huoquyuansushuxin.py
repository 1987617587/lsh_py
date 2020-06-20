import time

from selenium import webdriver

# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://www.baidu.com/')
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# input = browser.find_element_by_id('kw')
# print(input)
# print(input.get_attribute('name'))
# print(input.get_attribute('class'))
# print(input.get_attribute('id'))
# print(input.get_attribute('maxlength'))
# print(input.get_attribute('autocomplete'))

# 获取元素属性
elem = browser.find_element_by_partial_link_text('新闻')
print(elem)
print(elem.text)  # 必须是可见文本
print(elem.get_attribute('innerHTML'))  # 会返回元素的内部 HTML， 包含所有的 HTML 标签
print(elem.get_attribute('textContent'))  # 只会得到文本内容，而不会包含 HTML 标签
print(elem.get_attribute('innerText'))  # 只会得到文本内容，而不会包含 HTML 标签
time.sleep(3)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
browser.close()
# 关闭浏览器
browser.quit()
