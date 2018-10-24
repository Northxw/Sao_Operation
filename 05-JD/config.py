# -*- coding:utf-8 -*-

import os
import random

# 设备类型: Android 或 iOS
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
# DEVICE_NAME = 'MI_8'
DEVICE_NAME = 'vivo_X7'

# APP包名获取的前提:
#       打开手机上要获取的APP,命令行输入 adb shell, 接着输入 dumpsys activity | grep mFocusedActivity
#       前者为包名,后者为入口类型(其他方法自行百度)
APP_PACKAGE = 'com.jingdong.app.mall'

# 入口类型
APP_ACTIVITY = 'main.MainActivity'

# APP路径( 手机未安装京东APP时,修改启动参数,可通本地下载的apk文件安装再执行后续操作)
APP = os.path.abspath('.') + '/jd.apk'

# Appium 地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'

# 等待元素加载时间
TIMEOUT = 300

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700


# 滑动间隔(设置随机时间)
SCROLL_SLEEP_TIME = random.randint(3,7)

# 搜索关键词
KEYWORD = 'ipad'
