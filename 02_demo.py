# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 6:56 下午
# @Author  : Junjie Liu
# @Email   : junjie.liu@prmeasure.com
# @File    : 02_demo.py
# @Software: PyCharm

import time
import os
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

"""
查看当前activity
mActivityComponent
$ adb shell dumpsys activity activities

"""

# 切换搜狗输入法
command1 = "/usr/local/android-sdk-macosx/platform-tools/adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME\n"

desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "xxx",
    "appPackage": "tv.danmaku.bili",
    "appActivity": ".MainActivityV2",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
    # 'app': r'd:\apk\bili.apk',
}

# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(100)
# driver.quit()
# exit()
time.sleep(7)

# 根据id定位搜索位置框，点击
driver.find_element_by_id("expand_search").click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys('白月黑羽')
driver.press_keycode(AndroidKey.ENTER)

time.sleep(1)

screenSize = driver.get_window_size()
screenW = screenSize['width']
screenH = screenSize['height']
print("screenW:%s screenH:%s" % (screenW, screenH))
x = screenW / 2
# y1 = int(screenH * 0.8)
# y2 = int(screenH * 0.4)
y1 = 2055
y2 = 337

print(y1, y2, "\n---")

videos = []
for i in range(20):
    print("第%s页" % i)
    eles = driver.find_elements_by_id("title")
    for ele in eles:
        title = ele.text
        if title in videos:
            continue

        videos.append(title)
        print(title)

    # print('\n--------------\n')

    driver.swipe(start_x=253, start_y=y1, end_x=987, end_y=y2, duration=1300)

# input('**** 按任意键退出 ..')


print("--------------OK")
# for i in videos:
#     print(i)

# ret = os.popen(command1).read()
# print(ret)

driver.quit()
