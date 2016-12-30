# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:58:02 2016

@author: 101004679
说明：
- 演示如何使用Uiautomator模块
- 模块作者地址:https://github.com/kingdawin/uiautomator
"""

'''
导入uiautomator模块
from modname import funcname 
'''
from uiautomator import device as d

#d.wakeup
'''
拨打电话-退出
'''
d.press.home()
d(text="拨号").click()
d(description="一").click()
d(description="三").click()
d(description="六").click()
d(description="六").click()
d.press.back()
#d.sleep()

'''
设备信息
'''
deviceInfo=d.info
print "sdnInt="+str(deviceInfo['sdkInt'])

'''
滑动屏幕
'''
'向右滑'
d.swipe(100, 100, 500, 100, steps=10)







