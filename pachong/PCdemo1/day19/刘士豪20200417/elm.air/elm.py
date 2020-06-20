# -*- encoding=utf8 -*-
__author__ = "ljh"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
touch(Template(r"tpl1587124666356.png", record_pos=(0.344, -0.294), resolution=(1080, 2340)))
touch(Template(r"tpl1587211741325.png", record_pos=(-0.238, -0.134), resolution=(1080, 2340)))

time.sleep(5)
meishi_btn = poco(name="android.widget.ImageView") 
if meishi_btn.exists():
    meishi_btn.click()
    poco.swipe([0.5,0.8],[0.5,0.4])
    ls = poco(name='me.ele:id/sg')
    for each in ls:
        # 提取标题
        title = poco(name = 'me.ele:id/us')
        if title.exists():
            title = title.get_text()
        else:
             title = '空'
        print('title:',title)
        # 提取评分
        food_evaluate  = poco(name='me.ele:id/a3q')
        if food_evaluate.exists():
            food_evaluate = food_evaluate.get_text()
        else:
            food_evaluate = '空'
        print('food_evaluate:',food_evaluate)    
        # 提取月销售
        sell_nums = poco(name='me.ele:id/a3r')
        if sell_nums.exists():
            sell_nums = sell_nums.get_text()
        else:
            sell_nums = '0'
        print('sell_nums:',sell_nums)          
        # 提取配送价格信息
        send_money = poco(name='me.ele:id/a3s')
        if send_money.exists():
            send_money = send_money.get_text()
        else:
            send_money = '空'
        print('send_money:',send_money)  
        # 提取配送距离 时间
        send_time= poco(name='me.ele:id/a3u')
        if send_time.exists():
            send_time = send_time.get_text()
        else:
            send_time = '空'
        print('send_money:',send_time)  
        # 提取活动标签
        tag_list = []
        tag_text_ls = poco(name='com.sankuai.meituan:id/tag_text')
        if tag_text_ls.exists():
            for tag_text in tag_text_ls:
                tag_text = tag_text.get_text()
                tag_list.append(tag_text)
        else:
            tag_text_ls = '空'
        print('tag_list:',tag_list)
        # 提取优质评论信息
        comment_list = []
        comment_text_ls = poco(name='android.widget.TextView')
        if comment_text_ls.exists():
            for comment_text in comment_text_ls:
                comment_text = comment_text.get_text()
                comment_list.append(comment_text)
        else:
            comment_text = '空'
        print('comment_list:',comment_list)
        
        
        poco.swipe([0.5,0.6],[0.5,0.45])
        
       