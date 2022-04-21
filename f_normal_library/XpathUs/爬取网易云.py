# coding:utf-8
import requests
import urllib.request
from lxml import etree
import pprint
"""
知识点
1.Python爬虫
    1.去网页上面抓数据的程序
    2.通用：百度，谷歌，搜狗
    3.聚焦爬虫：针对性的去某个网站抓数据的程序
2.音乐网站爬取思路
3.xpath和正则的使用

百度音乐与网易云音乐区别在于：前者查看Network中的media，后者查看Network中的XHR，找到相关.m4a后缀的文件。

# 初步方法
url = "https://m701.music.126.net/20190708175635/cf5ffdfffb94953c15f837627210e49e/jdyyaac/525b/520e/0352/e1a3f3538fedf821e1ce4840e1083ba8.m4a"
base_url = "https://link.hhtjim.com/163/394556.mp3"
result  = requests.get(url).content
with open("./对面的女孩看过来.m4a","wb")as f:
    f.write(result)
    """
# 方法二
# 需要一步一步的尝试，从XHR，JS,CSS，media，最后到DOC，我们找到相关文件

# 确定url
music_url = "https://music.163.com/playlist?id=2817104628"

# 外链的链接（在判断语法之后写入）
base_url = "https://link.hhtjim.com/163/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
# 请求
req = urllib.request.Request(headers=headers,url=music_url)
qingqiu = urllib.request.urlopen(req)
html = qingqiu.read().decode("utf-8")
# print(html)
# 然后在本地获取到的地方寻找id

# 3 筛选数据
dom = etree.HTML(html)

# 使用Xpath语法获取所有歌曲id
ids = dom.xpath('//a[contains(@href,"song?")]/@href')
# pprint.pprint(ids)

# 4 遍历歌曲id
for music_id in ids:
    # 过滤切割
    # 获取歌曲的数字编号
    num_id = music_id.strip("/song?id=")
    # print(num_id)

# 测试（是否可以将$符号删除）
    # result = "$" in num_id
    # print(result)

# 判断语法，如果$符号在已获取的数字编号里，我们令他返回错误，因为不想要
    if ("$" in num_id) == False:
        # print(num_id)

        # 实现外链与歌曲数字编号的拼接
        song_url = base_url + "%s"%num_id + ".mp3"
        # print(song_url)
        # 再实现拼接后的切片
        song_name = song_url.split("/")[-1]
        print(song_name)

        # 获取数字编号的二进制文件
        music = requests.get(song_url).content
        # 保存本地文档

        with open("./歌单/%s"%song_name,"wb") as f:
            f.write(music)
