# -*- encoding=utf8 -*-
__author__ = "forwaiting"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)

touch(Template(r"tpl1590760159617.png", record_pos=(-0.115, -0.267), resolution=(1080, 2340)))

touch(Template(r"tpl1590760188586.png", record_pos=(0.246, -0.374), resolution=(1080, 2340)))


time.sleep(6)

touch(Template(r"tpl1590760253235.png", record_pos=(0.406, 0.48), resolution=(1080, 2340)))
time.sleep(3)
poco.swipe([0.5,0.9],[0.5,0.7])

for i in range(5):

    poco.swipe([0.5,0.8],[0.5,0.5])

    touch(Template(r"tpl1590760729373.png", record_pos=(0.216, 0.426), resolution=(1080, 2340)))

    time.sleep(11)
    touch(Template(r"tpl1590761238993.png", record_pos=(-0.431, -0.948), resolution=(1080, 2340)))


    
