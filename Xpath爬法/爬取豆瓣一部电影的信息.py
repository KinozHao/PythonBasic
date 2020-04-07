import requests
from lxml import etree
import time
"""
requests和lxml是常见新手入门的爬虫包
简单的一个爬取 爬取一个网页的html数据
url = "https://blog.csdn.net/mtbaby/article/details/79164234"
data = requests.get(url)
data.encoding='utf-8'
print(data.text)
"""

url = "https://movie.douban.com/subject/26794435/"
data = requests.get(url).text
#requests包下的get方法: 	获取HTML网页的主要方法，对应于HTTP的GET

s = etree.HTML(data)
# 给定url并用requests.get()方法来获取页面的text，用etree.HTML()
# 来解析下载的页面数据“data”。


file_name = s.xpath('//*[@id="content"]/h1/span[1]/text()')       #电影名字
director = s.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')          #编剧

actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')    #主演


move_time = s.xpath('//*[@id="info"]/span[15]/text()')    #片长

star = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')   #豆瓣评分

#由于编剧有时候不止一个人，所以我这里以列表的形式输出
ds = []
for d in director:
    ds.append(d)

#由于演员不止一个人，所以我这里以列表的形式输出
acs = []
for a in actor:
    acs.append(a)

print ('电影名:',file_name)
print ('编剧:',director)
print ('主演:',actor)
print ('片长:',move_time)
print('评分:',star)
