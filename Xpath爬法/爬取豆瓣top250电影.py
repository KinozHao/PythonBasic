import requests
import time
from lxml import etree

print("*"*20)
print("豆瓣TOP250电影爬取器V0.01")
print("*"*20)

for a in range(10):
    url = "https://movie.douban.com/top250?start={}".format(a*25)
    data = requests.get(url).text
    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')

    """
    //*[@id="content"]/div/div[1]/ol/li[1]      整体
    //*[@id="content"]/div/div[1]/ol/li[1]  /div/div[2]/div[1]/a/span[1]  电影名字
    //*[@id="content"]/div/div[1]/ol/li[1]  /div/div[2]/div[2]/div/span[2] 评分
    """
    for div in file:
        name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        start = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        comment = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')
        num = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0].strip('(').strip().strip(')')
        href = div.xpath('./div/div[2]/div[1]/a/@href')[0]

        if len(comment) > 0:
            print("{}--->{}--->{}--->{}--->{}".format(name,start,comment,num,href))
        else:
            print("{}--->{}--->{}--->{}".format(name,start,num,href))
        print('\n')


print("="*20)
print("以上是豆瓣TOP250的图书")
print("="*20)
