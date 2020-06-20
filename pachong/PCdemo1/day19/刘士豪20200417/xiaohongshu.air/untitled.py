# -*- encoding=utf8 -*-
__author__ = "ljh"

from airtest.core.api import *

import time

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


touch(Template(r"tpl1587088647990.png", record_pos=(-0.113, 0.601), resolution=(1080, 2340)))

time.sleep(6)
ls = poco(name='com.xingin.xhs:id/ax2')
if not ls.exists():
    print('no note exists.')
else:
    for i in range(3):
        # 首页下拉三次（大概12个作品）
        for each in ls:
    #         if poco(name="com.xingin.xhs:id/ar3"):
    #             print("这是视频")
    #             each.click() # 进入详情
    #         else:
    #             each.click() # 进入详情
    #             # 向上滚动页面(如果是视频不需要滚动)
            each.click() # 进入详情
    #         poco.swipe([0.5,0.8],[0.5,0.3])
            # 提取标题
            title = poco(name = 'com.xingin.xhs:id/br8')
            if title.exists():
                title = title.get_text()
            else:
                title = poco(name = 'com.xingin.xhs:id/noteContentText')
                if title.exists():
                    title = title.get_text()
                else:
                    title = '空'
            print('title:',title)
            # 提取昵称
            nickname = poco(name='com.xingin.xhs:id/nickNameTV')
            if nickname.exists():
                nickname = nickname.get_text()
            else:
                nickname = poco(name='com.xingin.xhs:id/matrixNickNameView')
                if nickname.exists():
                    nickname = nickname.get_text()
                else:
                    nickname = '空'
            print('nickname:',nickname)    
            # 提取点赞数
            support_nums = poco(name='com.xingin.xhs:id/bq_')
            if support_nums.exists():
                support_nums = support_nums.get_text()
            else:
                support_nums = poco(name='com.xingin.xhs:id/likeTextView')
                if support_nums.exists():
                    support_nums = support_nums.get_text()
                else:
                    support_nums = '0'
            print('support_nums:',support_nums)          
            # 提取收藏数
            faviole_nums = poco(name='com.xingin.xhs:id/bpd')
            if faviole_nums.exists():
                faviole_nums = faviole_nums.get_text()
            else:
                faviole_nums = poco(name='com.xingin.xhs:id/xk')
                if faviole_nums.exists():
                    faviole_nums = faviole_nums.get_text()
                else:
                    faviole_nums = '0'
            print('faviole_nums:',faviole_nums)          
            # 提取评论数
            comment_nums = poco(name='com.xingin.xhs:id/bpj')
            if comment_nums.exists():
                comment_nums = comment_nums.get_text()
            else:
                comment_nums = poco(name='com.xingin.xhs:id/commentTextView')
                if comment_nums.exists():
                    comment_nums = comment_nums.get_text()
                else:
                    comment_nums = '0'
            print('comment_nums:',comment_nums)    

            # 提取笔记内容
            content = poco(name='com.xingin.xhs:id/alj')
            if content.exists():
                content = content.get_text()
            else:
                content = poco(name='com.xingin.xhs:id/noteContentText')
                if content.exists():
                    content = content.get_text()
                else:
                    content = '0'
            print('content:',content)    
            # 返回
            black_btn = poco(name="com.xingin.xhs:id/jt")
            if black_btn.exists():
                black_btn.click()
            else:
                # print('error...')
                # 向左滑动页面
                # poco.swipe([0.8,0.5],[0.2,0.5])
                black_btn = poco(name="com.xingin.xhs:id/backButton")
                if black_btn.exists():
                    black_btn.click()
                else:
                    print('error...')

        # 向上滑动屏幕
        poco.swipe([0.5,0.8],[0.5,0.3])
        poco.swipe([0.5,0.8],[0.5,0.4])




