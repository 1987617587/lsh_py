from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds
driver.get("http://www.jinvjie.com/t-list-52.html")
mainbody = driver.find_element_by_id("mainbody")
print(mainbody)