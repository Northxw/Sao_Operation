# -*- coding：utf-8 -*-
"""
Created at 8:48 on Oct 23,2018
@author: Northxw
@title: 模拟登录微信并获取朋友圈数据
@precautions: 代码中所有的节点都须提前通过Appium新建Session获取(亲测vivo_x7和Mi_8节点相同,其余机型未知)
"""

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
from peocessor import Processor
from time import sleep
from config import *

class Moments(object):
    def __init__(self):
        """
        初始化
        """
        # 启动APP的参数配置
        self.desired_caps = {
            'platformName': PLANTFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)            # 创建Mongo数据库的链接对象
        self.db = self.client[MONGO_DB]                 # 指定数据库
        self.collection = self.db[MONGO_COLLECTION]     # 指定集合
        # 处理日期
        self.processor = Processor()

    def login(self):
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/drp')))
        login.click()
        # 手机号码输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        phone.set_text(USERNAME)
        # 下一步
        next = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ast')))
        next.click()

        sleep(20)   # 点击下一步后，(本人)手机获取密码输入框节点较慢，设置延时等待，否则KeyError
        
        # 密码
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        password.set_text(PASSWORD)
        # 提交
        submit = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ast')))
        submit.click()

        sleep(15)   # 点击提交后，会加载是否匹配通讯录好友的选择框，延时等待，否则KeyError

        # 通讯录匹配提示(这里选"否",加快tab节点的加载速度)
        determine = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/au9')))
        determine.click()

    def enter(self):
        sleep(120)   # 1.通讯录匹配后进入微信,会加载微信本地数据,耗时较长,设置延时等待(等待tab节点完全加载出来,可灵活配置等待时间)
                     # 2.等待加载数据的过程,可能会闪退微信,可手动点击重新进入.
                     # 3.亲测vivo_x7和MI_8重新登录微信并加载本地数据的耗时基本相同.
                     # 4.请勿在多台安卓设备上登录微信,可能会通过手机号无法登录的结果(亲测)
        # 选项卡
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/azn')))
        tab.click()
        # 朋友圈
        momnets = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/agp')))
        momnets.click()
        sleep(10)   # 延迟10秒,等待朋友圈数据刷新

    def crawl(self):
        while True:
            # items存储当前手机界面的所有朋友圈.
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/e6t"]//android.widget.FrameLayout')))   # 每个e6t节点对应一条朋友圈数据
            # 上滑刷新朋友圈
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('comment.tencent.mm:id/azl').get_attribute('text')   # 可通过Appium新建Session获取正文的节点ID
                    # 正文
                    content = item.find_element_by_id('comment.tencent.mm:id/jv').get_attribute('text')     # 同上
                    # 日期
                    date = item.find_element_by_id('comment.tencent.mm:id/e25').get_attribute('text')       # 同上
                    # 处理日期
                    date = self.processor.date(date)    
                    print(nickname, content, date)
                    data = {
                        'nickname': nickname,
                        'content': content,
                        'date': date,
                    }
                    # 根据昵称和正文来查询信息,然后设置第三个参数为True.实现存在就更新,不存在就插入数据
                    self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)    # 上滑延迟
                except NoSuchElementException:
                    pass

    def main(self):
        """
        入口
        :return:
        """
        # 登录
        self.login()
        # 进入朋友圈
        self.enter()
        # 爬取
        self.crawl()

if __name__ == '__main__':
    moments_ = Moments()
    moments_.main()
