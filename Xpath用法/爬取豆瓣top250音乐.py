import requests
import time     # 时间模块是为了防止网站封你的ip
from lxml import etree


url = "https://music.douban.com/top250"
data = requests.get(url).text       # get方法用来获取页面的text
s = etree.HTML(data)     # etree.HTML解析下载页面的数据 就是定义的data


name = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')[0]
single = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/p/text()')[0]
start = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]/text()')[0]
comment = s.xpath('//*[@id="content"]/div/div[1]/div/table[2]/tr/td[2]/div/div/span[3]/text()')[0]
print('Name:',name)
print('Single:',single)
print('Start:',start)
print('Comment:',comment)

if len(comment) > 0:
    print("{}--->{}--->{}--->{}".format(name, single, start, comment))
else:
    print("{}--->{}--->{}".format(name, single, start))
print('\n')