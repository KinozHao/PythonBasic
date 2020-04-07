#获取网页
import pprint
import re
import requests

#请求网页
content = requests.get("https://book.douban.com/").text

#解析网页中内容（用正则）
sq = re.compile('<li.*?title="(.*?)".*?href="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>', re.S)

#获取到当前网页中全部的相关内容
result = re.findall(sq,content)

#print(result)
#pprint.pprint(result)

for i in result:
    name,url,author,year,publisher = i
    author = re.sub("\s","",author)
    year = re.sub("\s","",year)
    publisher = re.sub("\s","",publisher)
    print(name,url,author,year,publisher)
#保存到本地




