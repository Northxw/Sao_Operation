# -*- coding:utf-8 -*-

import urllib.request
from pyquery import PyQuery as pq
from utils.config import *

class Get_Download_Url(object):
    def __init__(self, keyword=KEYWORD, url=URL, headers=HEADERS):
        """
        初始化信息
        :param keyword: 搜索关键字
        :param url: 搜索链接
        """
        self.url = url + keyword.replace(' ', '%20')    # 转换为URL编码格式.
        # print(self.url)
        self.headers = headers    # 设置请求头.
        
    def request(self):
        """
        发送请求，返回网页数据
        :return: 网页源码
        """
        request_ = urllib.request.Request(url=self.url, headers=self.headers)  # 构建Request类
        response = urllib.request.urlopen(request_)     # 发送请求,返回结果
        if response.status == 200:
            return response
        else:
            print('Something Wrong!')

    def parse(self, response):
        """
        解析网页, 返回下载页的URL
        :param response: 网页源码
        :return: App下载页面的URL
        """
        download_detail_url = ''    # 接收下载详情页的链接
        html = response.read()
        doc = pq(html)      # 使用pyquery解析网页
        a = doc('#Mlist > div:nth-child(1) > a').items()  # 返回第一个App栏的a标签元素的位置
        for _ in a:
            try:
                download_detail_url = 'http://www.duote.com{}'.format(_.attr('href'))     # 格式化URL
            except Exception:
                print('Something Wrong!')
        return download_detail_url

    def get(self, url):
        """
        获取下载详情页中Apk的下载链接
        :param url: 下载详情页的URL
        :return: apk的下载URL
        """
        apk_downlaod_url = ''
        response = urllib.request.urlopen(url)  # 发送请求,返回结果
        doc = pq(response.read())
        href = doc('.apk_info_box .dl_area .btn_trig #quickDown').items()
        for _ in href:
            apk_downlaod_url = _.attr('href')
            break
        return apk_downlaod_url

    def download_url(self):
        """
        合并、简化函数
        :return: 手机应用的下载链接
        """
        response = self.request()   # 发送请求
        download_detail_url = self.parse(response)  # 解析网页
        apk_download_url = self.get(download_detail_url)    # 获取下载链接
        return apk_download_url

if __name__ == '__main__':
    app = Get_Download_Url()
    app.download_url()
