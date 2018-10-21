# -*- coding:utf-8 -*-
"""
Created at 18:31 on Oct 10,2018
@title: 本地安装APP（提前下载要安装的APP）
@author：Northxw
"""

from appium import webdriver
from App_For_Android.utils.config import *
import os

# 获取当前项目的根路径
APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
# 安装路径
APP_VALUE = APP_PATH + '\\app\\MoJi_Weather.apk'    # 测试安装墨迹天气

class Install(object):
    def __init__(self, server=SERVER, platformname=PLANTFORM, devicename=DEVIDE_NAME, app_value=APP_VALUE):
        """
        初始化信息
        :param server: Appium Server
        :param platformname: 手机类型：安卓 | IOS
        :param devicename: 设备名称
        :param app_value: 安装路径
        """
        self.server = server
        self.platformname = platformname
        self.devicename = devicename
        self.app_value = app_value

    def install(self):
        """
        从PC端App仓库安装软件到手机（一般放在根目录下的某个文件，方便检索）
        :return: None
        """
        desired_caps = {  # 配置安装启动App的参数
            'platformName': self.platformname,
            'deviceName': self.devicename,
            'app': self.app_value,
        }
        try:
            driver = webdriver.Remote(self.server, desired_caps)
        except Exception as e:
            _ = e
        print('Something Wrong!')

if __name__ == '__main__':
    install = Install()
    install.install()