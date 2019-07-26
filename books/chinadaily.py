#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook # 继承基类BaseFeedBook

# 返回此脚本定义的类名
def getBook():
    return ChinaDaily

# 继承基类BaseFeedBook
class ChinaDaily(BaseFeedBook):
    # 设定生成电子书的元数据
    title = u'China Daily' # 设定标题
    __author__ = u'China Daily' # 设定作者
    description = u'Chinadaily.com.cn is the largest English portal in China. ' # 设定简介
    language = 'en' # 设定语言

    # 指定要提取的包含文章列表的主题页面链接
    # 每个主题是包含主题名和主题页面链接的元组
    feeds = [
        (u'National affairs', 'http://www.chinadaily.com.cn/china/governmentandpolicy'),
        (u'Society', 'http://www.chinadaily.com.cn/china/society'),
    ]
