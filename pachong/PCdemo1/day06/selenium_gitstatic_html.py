"""
加载本地html
"""
from selenium import webdriver
import os
browser = webdriver.Chrome()
browser.get('file:///'+os.path.abspath('dongman.html'))
print(browser.title)