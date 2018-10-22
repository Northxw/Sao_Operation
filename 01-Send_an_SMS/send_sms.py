# -*- coding:utf-8 -*-
"""
Created at 23:16 on Oct 19,2018
@title: 使用Twilio自动发送短信
@author: Northxw
"""

from twilio.rest import Client
from datetime import datetime
from traceback import format_exc
from .utils.config import *

class Sms(object):
    def __init__(self, account=TWILIO_ACCOUNT_SID, token=TWILIO_AUTH_TOKEN):
        """
        初始化信息
        :param account: Your Twilio Account SID
        :param token: Your Twilio Auth TOKEN
        """
        self.account = account
        self.token = token
        self.client = Client(self.account, self.token)  # 初始化Client对象

    def parse_date(self):
        """
        格式化日期
        :return: 格式化后的当前日期.例如：2018-10-19
        """
        format_now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(' ')[0]
        return format_now_date

    def send(self):
        """
        根据日期向特定人发送问候留言
        :return: None
        """
        target_date = self.parse_date()     # 目标日期(特定日期,比如情人节)
        for name, date in DATE.items():
            if date == target_date:                           # 遍历DATE字典,判断目标日期是否包含在DATE.keys()
                body = name + ', ' + BODY                     # 根据节日不同, 发送内容不同的短信
                phone_number = CONTACT_PHONE_NUMBER[name]     # 设置接收短信者
                try:
                    self.client.messages.create(
                        to=phone_number,
                        from_=TWILIO_NUMBER,
                        body=body)
                except Exception as e:
                    _ = e                   # 接收异常(_符号总是记录最近的改变)
                    # print(format_exc())
                    print('Failed!')
                else:
                    print('Successfully!')

if __name__ == '__main__':
    sms = Sms()     # 创建Sms类对象
    sms.send()      # 发送信息
