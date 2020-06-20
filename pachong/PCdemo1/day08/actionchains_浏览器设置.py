import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
# 禁止图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)
# 无界面浏览器
options.add_argument('--headless')
# 或者
# options.set_headless()
# 添加代理 ip
# options.add_argument("--proxy-server=http://202.20.16.82:10152")
# 添加 UA
options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn;\
MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0\
Mobile Safari/533.1"')
# 创建定制选项的浏览器对象
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.baidu.com')
time.sleep(5)
print(browser.page_source)
browser.quit()