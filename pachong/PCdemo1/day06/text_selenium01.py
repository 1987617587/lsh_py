from selenium import webdriver
# 生成浏览器对象
browser = webdriver.Chrome()
# 请求页面
browser.get('https://www.baidu.com')

# 打印网页渲染后的源代码
print(browser.page_source)
# 打印页面标题 "百度一下，你就知道"
print(browser.title)
# 获取当前 url
print(browser.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
browser.close()
# 关闭浏览器
browser.quit()


