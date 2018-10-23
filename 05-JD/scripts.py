# -*- coding:utf-8 -*-
"""
Created at 00:00 on Oct 23,2018
@title: 使用Appium和mitmdump自动获取京东APP的商品数据
@tip: 获取节点ID阶段,设置了较多的sleep(time),为了节点能够完全加载出来(可根据手机的CPU灵活调整)
@author: Northxw
@reference: Python3网络爬虫开发实战-崔庆才
"""

import re
import json
from urllib.parse import unquote
import pymongo

client = pymongo.MongoClient('localhost')   # 创建连接对象
db = client['jd']                           # 指定数据库
comments_collection = db['comments']        # 指定评论信息集合
products_collection = db['products']        # 指定商品数据集合

def response(flow):
    global comments_collection, products_collection
    # 提取评论数据
    url = 'api.m.jd.com/client.action'
    if url in flow.request.url:
        pattern = re.compile('sku\".*?\"(\d+)\"')
        # Request请求参数中包含商品ID
        body = unquote(flow.request.text)
        # 提取商品ID
        id = re.search(pattern, body).group(1) if re.search(pattern, body) else None
        # 提取Response Body
        text = flow.response.text
        data = json.loads(text)     # 将json字符串转换为json对象
        comments = data.get('commentInfoList') or []    # 如果没有获取到评论信息,就赋值空列表
        # 提取评论数据
        for comment in comments:
            if comment.get('commentInfo') and comment.get('commentInfo').get('commentData'):
                info = comment.get('commentInfo')
                text = info.get('commentData')
                date = info.get('commentDate')
                nickname = info.get('userNickName')
                pictures = info.get('pictureInfoList')
                print(id, nickname, text, date)
                comments_collection.insert({    # 插入评论详情页的单条数据
                    'id': id,
                    'text': text,
                    'date': date,
                    'nickname': nickname,
                    'pictures': pictures
                })

    url = 'cdnware.m.jd.com'        # 包含商品图片,名称和ID的接口
    if url in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        if data.get('wareInfo') and data.get('wareInfo').get('basicInfo'):  # wareInfo的basicInfo字段包含了所需要的信息字段.
            info = data.get('wareInfo').get('basicInfo')
            id = info.get('wareId')             # 商品ID
            name = info.get('name')             # 商品名称
            images = info.get('wareImage')      # 商品图片(只获取图片链接,不保存二进制数据)
            print(id, name, images)
            products_collection.insert({    # 插入商品列表的单条数据
                'id': id,
                'name': name,
                'images': images
            })