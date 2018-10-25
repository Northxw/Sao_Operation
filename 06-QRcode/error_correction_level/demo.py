# -*- coding:utf-8 -*-

import os
from MyQR import myqr

# 链接或者文字
words = 'http://github.com/Northxw'
# words = 'Hello, Welcome to here!'

# 示例：生成两张纠错等级不同的普通二维码
def test1():
    version, level, qr_name = myqr.run(
                            words,
                            version=1,
                            level='L',              # 纠错等级(L,M,Q,H)
                            picture=None,           # 图片路径或图片
                            colorized=True,         # 彩色
                            contrast=1.0,           # 对比度
                            brightness=1.0,         # 亮度
                            save_name='L.jpg',      # 文件名称
                            save_dir=os.getcwd()    # 存储路径
                            )

# 因为是同时生成两张图片,所以修改生成图片名称.
def test2():
    version, level, qr_name = myqr.run(
                            words,
                            version=1,
                            level='H',              # 纠错等级(L,M,Q,H)
                            picture=None,           # 图片路径或图片
                            colorized=True,         # 彩色
                            contrast=1.0,           # 对比度
                            brightness=1.0,         # 亮度
                            save_name='H.jpg',      # 文件名称
                            save_dir=os.getcwd()    # 存储路径
                            )
    # print(version, level, qr_name)

test1()
test2()