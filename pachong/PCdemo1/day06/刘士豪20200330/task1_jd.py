"""
案例：提取京东商品的价格
https://www.jd.com/

"""
import random
import time

from selenium import webdriver


def search(good_name, url):
    try:
        browser = webdriver.Chrome()
        # 窗口最大化
        browser.maximize_window()
        browser.get(url)
        time.sleep(2)
        elem_good = browser.find_element_by_id('key')
        # 清除搜索框内容
        elem_good.clear()
        # print("请输入搜索的商品名称：")

        elem_good.send_keys(good_name)
        time.sleep(3)

        print('点击搜索')
        submit_btn = browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        submit_btn.click()
        print("正在进入搜索结果页面")
        time.sleep(3)
        crawl(browser)



    except Exception as e:
        print(e, "请求失败")
        return None


def crawl(browser):
    try:
        print("当前进入链接为：", browser, browser.current_url)
        # 返回页面的高度
        last_height = browser.execute_script('return document.body.scrollHeight;')
        while True:
            print("页面向下加载中……")
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            # 等待随机时间
            time.sleep(random.random() * 2 + 3)
            # 计算滚动之后的页面高度
            new_height = browser.execute_script('return document.body.scrollHeight;')
            print("当前页面高度", new_height)
            if new_height == last_height:
                print("到底了")
                break
            last_height = new_height

        print("加载结束")
        print("开始提取信息")
        # ls = browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        ls = browser.find_elements_by_css_selector('.gl-item')
        print('len', len(ls))
        for good in ls:
            # //*[@id="J_goodsList"]/ul/li[46]/div/div[1]/a/img
            # good_img = good.find_element_by_xpath('.//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/img').get_attribute(
            #     'src')
            good_img = good.find_element_by_css_selector('div.gl-i-wrap > div.p-img > a > img').get_attribute('src')
            if not good_img:
                # 图片懒加载 data-lazy-img 这个需要拼接完整路径
                good_img = good.find_element_by_css_selector('div.gl-i-wrap > div.p-img > a > img').get_attribute(
                    'data-lazy-img')
            print(f"good_img:{good_img}")
            good_price = good.find_element_by_xpath('.//div/div[2]/strong/i').text.strip()
            print(f"good_price:{good_price}")
            good_dice = good.find_element_by_xpath('.//div/div[@class="p-name p-name-type-2"]/a/em').text.strip()
            print(f"good_dice:{good_dice}")
            comment_nums = good.find_element_by_xpath('.//div[@class="p-commit"]//a').text.strip()
            print(f"comment_nums:{comment_nums}")
            good_shop = good.find_element_by_xpath('.//div/div[@class="p-shop"]/span/a').text.strip()
            print(f"good_shop:{good_shop}")
            print("=" * 66)
        time.sleep(5)
        print("正在查找下一页链接和按钮")
        next_page_btn = browser.find_element_by_xpath(
            '//*[@id="J_bottomPage"]/span[@class="p-num"]/a[@class="pn-next"]')
        if next_page_btn:
            print("点击下一页")
            next_page_btn.click()
            time.sleep(5)
            # 继续获取下一页
            crawl(browser)
        else:
            browser.close()


    except Exception as e:
        print("请求失败", e)


if __name__ == '__main__':
    good_name = "无人机"

    url = 'https://www.jd.com/'
    search(good_name, url)
