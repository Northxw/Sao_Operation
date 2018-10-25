# -*- coding:utf-8 -*-

import os
from MyQR import myqr

# 链接或者文字(以Github为例)
words = 'http://github.com/Northxw'
# words = 'Hello, Welcome to here!'

# 示例：生成彩色动态二维码
version, level, qr_name = myqr.run(
                        words,
                        version=1,
                        level='H',              # 纠错等级(L,M,Q,H)
                        picture='./520.gif',    # 图片路径或图片
                        colorized=True,         # 彩色
                        contrast=1.0,           # 对比度
                        brightness=1.0,         # 亮度
                        save_name='./520_qrcode.gif',     # 存储名称
                        save_dir=os.getcwd()    # 存储路径
                        )
