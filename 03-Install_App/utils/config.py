# -*- coding:utf-8 -*-

# Appium服务(默认监听本地4723端口,可以发送命令进行交互)
SERVER = 'http://localhost:4723/wd/hub'

# 设备类型(Android 或 iOS)
PLANTFORM = 'Android'

# 设备名称
DEVIDE_NAME = 'vivo_X7'

# APP包名(可通过手机连接PC,开启USB调试,进入手机文件查找)
APP_PACKAGE = 'com.tencent.mm'

# 入口类名
APP_ACTIVITY = '.ui.LauncherUI'

# 搜索关键词(这里用TIM做测试)
KEYWORD = 'TIM'

# 2345安置市场的搜索URL
URL = 'http://www.duote.com/searchandroid/index?keywords='

# 设置headers
HEADERS = {
    'Cookie': 'Hm_lvt_4aa2af3ba32bf53eba883d71ab4a699e=1540050409,1540088091; PHPSESSID=b09918506e679d951341700b2e2dc25a; Hm_lvt_9d747685daa8f5b96d8c4140aa23ffe8=1540088138; Hm_lpvt_9d747685daa8f5b96d8c4140aa23ffe8=1540088680; Hm_lpvt_4aa2af3ba32bf53eba883d71ab4a699e=1540088680',
    'Referer': 'http://www.duote.com/android/',
    'Host': 'www.duote.com',
}
