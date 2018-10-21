# -*- coding:utf-8 -*-
"""
Create at 19:03 on Oct 21,2018
@title: 在线安装App
@author: Northxw
"""

from appium import webdriver
from .utils.config import *
from .utils.url import Get_Download_Url

APP_VALUE = Get_Download_Url().download_url()   # 创建下载链接的对象并初始化

class Install(object):
    def __init__(self, server=SERVER, app_value=APP_VALUE, platformname=PLANTFORM, devicename=DEVIDE_NAME):
        """
        初始化信息
        :param server: Appium Server
        :param app_value: Apk 文件的下载链接
        """
        self.server = server
        self.app_value = app_value
        self.platformname = platformname
        self.devicename = devicename

    def install(self):
        """
        启动安装程序
        :return: None
        """
        desired_caps = {                # 配置安装启动App的参数
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
