# -*- encoding=utf8 -*-
__author__ = "forwaiting"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

touch(Template(r"tpl1590760159617.png", record_pos=(-0.115, -0.267), resolution=(1080, 2340)))

touch(Template(r"tpl1590761358552.png", record_pos=(-0.001, -0.376), resolution=(1080, 2340)))
poco.wait_for_all

time.sleep(3)
touch(Template(r"tpl1590761484189.png", record_pos=(-0.306, -0.939), resolution=(1080, 2340)))


# text("瓜分10亿")
text("618列车")
time.sleep(5)
poco.swipe([0.5,0.9],[0.5,0.4])
poco.swipe([0.5,0.9],[0.5,0.4])

poco.wait_for_all

ls = poco(name='android.view.View',touchable =  True)
print(len(ls))

if len(ls) > 0:

    for each in ls:
        if each.exists():
            each.click()
            poco.swipe([0.5,0.9],[0.5,0.2])
            time.sleep(17)
            poco.swipe([0.01,0.5],[0.6,0.5])
            time.sleep(1)

        
            poco.swipe([0.5,0.6],[0.5,0.4])
else:
    poco.swipe([0.5,0.9],[0.5,0.2])
            
