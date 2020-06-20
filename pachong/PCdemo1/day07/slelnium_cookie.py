from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.youdao.com'
browser.get(url)
# 获取cookie信息
cookies = browser.get_cookies()
print(cookies)
# 添加cookie信息
browser.add_cookie({'name': 'key-666', 'value': 'value-16541154'})
# 删除cookie信息
# browser.delete_cookie('key-666')
browser.delete_all_cookies()
# 遍历cookie
for cookie in browser.get_cookies():
    print('name', cookie['name'], 'value', cookie['value'])
browser.close()
