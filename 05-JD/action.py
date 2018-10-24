# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import *

class Action(object):
    def __init__(self):
        # 驱动配置
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)    # 创建driver
        self.wait = WebDriverWait(self.driver, TIMEOUT)                     # 设置显式等待时间

    def comments(self):
        global comments_tab
        sleep(10)
        # 同意京东隐私政策
        button_scheme = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/bt1')))
        button_scheme.click()

        # 允许京东使用网络定位(MI_8需要确认,vivo_X7不需要)
        # button_area = self.wait.until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        # button_area.click()

        # 延时等待10秒, 等待"双十一"动画界面完全加载(非双11,双12期间应该没有该界面)
        sleep(15)
        close_animation_button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/r7')))
        close_animation_button.click()
        # 延时等待10秒, 等待关闭动画界面后,节点可以完全加载出来(时间可以根据情况灵活配置)
        sleep(10)
        # 进入搜索页面
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/r6')))
        search.click()
        # 输入搜索文本
        box = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.search:id/search_text')))
        box.set_text('ipad2018')    # 搜索关键字
        sleep(10)
        # 点击搜索按钮
        button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/au1')))
        button.click()
        sleep(10)
        # 点击进入商品详情页
        view = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.search:id/product_list_item')))
        view.click()
        sleep(10)

        # 处理: 直接进入详情页无法查找到pd_tab3的节点,可通过上滑刷新到全部评论的位置,点击进入,效果相同;此时pa_tab3也会加载出来)
        # 向下滑动查找评论节点(测试发现,需要滑动屏幕三次)
        cnt = 1
        while True:
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(SCROLL_SLEEP_TIME)
            cnt = cnt + 1
            if cnt > 3:
                break

        # 滑动结束,延时等待
        sleep(10)
        # 判断节点是否出现,出现执行下一步,未出现继续下滑.
        if self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_comment_title'))):
            comments_tab_1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_comment_title')))
            comments_tab_1.click()
        if self.wait.until(EC.presence_of_element_located((By.ID, 'com.jb.lib.productdetail:id/pd_tab3'))):
            comments_tab_2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jb.lib.productdetail:id/pd_tab3')))
            comments_tab_2.click()
            # 点击进入评论详情页
        sleep(10)

    def scroll(self):
        while True:
            # 模拟拖动
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(SCROLL_SLEEP_TIME)    # 滑动间隔时间

    def main(self):
        self.comments()
        self.scroll()

if __name__ == '__main__':
    action = Action()
    action.main()