# -*- encoding=utf8 -*-
__author__ = "ljh"

from airtest.core.api import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



auto_setup(__file__)
touch(Template(r"tpl1587124666356.png", record_pos=(0.344, -0.294), resolution=(1080, 2340)))
touch(Template(r"tpl1587124675168.png", record_pos=(0.001, -0.145), resolution=(1080, 2340)))
time.sleep(3)
meishi_btn = poco(name="美食") 
if meishi_btn.exists():
    meishi_btn.click()
    poco.swipe([0.5,0.8],[0.5,0.3])
    ls = poco(name='android.widget.FrameLayout')
    for each in ls:
        # 提取标题
        title = poco(name = 'com.sankuai.meituan:id/poi_name')
        if title.exists():
            title = title.get_text()
        else:
             title = '空'
        print('title:',title)
        # 提取评分
        food_evaluate  = poco(name='com.sankuai.meituan:id/food_poi_item_evaluate')
        if food_evaluate.exists():
            food_evaluate = food_evaluate.get_text()
        else:
            food_evaluate = '空'
        print('food_evaluate:',food_evaluate)    
        # 提取人均消费
        avg_price = poco(name='com.sankuai.meituan:id/avg_price')
        if avg_price.exists():
            avg_price = avg_price.get_text()
        else:
            avg_price = '0'
        print('avg_price:',avg_price)          
        # 提取标签
        cate_tag_name = poco(name='com.sankuai.meituan:id/cate_tag_name')
        if cate_tag_name.exists():
            cate_tag_name = cate_tag_name.get_text()
        else:
            cate_tag_name = '空'
        print('cate_tag_name:',cate_tag_name)  
        # 提取标签2
        tag_text = poco(name='com.sankuai.meituan:id/tag_text')
        if tag_text.exists():
            tag_text = tag_text.get_text()
        else:
            tag_text = '空'
        print('tag_text:',tag_text)
        # 提取优惠信息
        discount_text = poco(name='com.sankuai.meituan:id/discount_text')
        if discount_text.exists():
            discount_text = discount_text.get_text()
        else:
            discount_text = '空'
        print('discount_text:',discount_text)
        poco.swipe([0.5,0.6],[0.5,0.4])
        
       




