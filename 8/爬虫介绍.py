# 大麦网 拉勾网  图虫网 网易云
"""
import urllib.request       # urllib python內部的请求库

print(urllib.request.urlopen("http://baidu.com"))   # 返回百度网址的response


import requests

print(requests.get("http://baidu.com"))


from selenium import webdriver      # python自动获取到网页

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.get("http://www.zhihu.com")
driver.get("http://www.taobao.com")
"""

from bs4 import BeautifulSoup #Lxml 解析网页h或是解析网页中的内容
soup = BeautifulSoup("<p>Hello world</p>","lxml")
print(soup)
# 怎么保存数据 ?
# 1 文本(纯文本,Json,XML)
# 2 关系型数据库(MySql,Oracle,SqlSever)具有结构化的表格
# 3 非关系型数据库(MongoDB,Redis  key---value形式)
# 4 二进制文件(图片,音频,视频等等)保存成特定格式的

# Pyquery

from pyquery import PyQuery as pq

doc = pq("<html><head><title>Hello world</title></head></html>")
result = doc("html").text()
print(result)

# Python常用的框架 Flask(小型的开源框架,大多数用于开发自己的个人博客),Django(知乎,豆瓣)
