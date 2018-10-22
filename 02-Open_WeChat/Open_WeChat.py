# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 指定 Appium Server
server = 'http://localhost:4723/wd/hub'

# 配置 Desired Capabilities (启动APP的参数)
desired_caps = {
    'platformName': 'Android',  # 设备类型，分为Android或iOS
    'deviceName': 'vivo_X7',    # 设备名称
    'appPackage': 'com.tencent.mm',     # App包名
    'appActivity': '.ui.LauncherUI'     # 入口
}

# 新建 Session(与点击Appium内置的Start Session按钮的功能相同)
driver = webdriver.Remote(server, desired_caps)

wait = WebDriverWait(driver, 30)    # 设置页面加载等待,保证所有节点完全加载出来
login = wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/drp')))    # 微信欢迎页面登录按钮
login.click()
phone_password = wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))     # 输入手机号的文本栏
phone_password.set_text('***********')
next_login = wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ast')))     # 下一步
next_login.click()
phone_password.send_keys('********')    # 密码输入框的ID和手机号输入框的ID相同,所以不重复获取

try:
    next_login.click()          # 最后的登录按钮ID与欢迎界面的登录按钮的ID相同,不重复获取
except Exception as e:
    _ = e
    print('Incorrect username or password !')
