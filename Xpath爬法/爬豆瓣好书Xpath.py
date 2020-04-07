import requests
from lxml import etree
import time

url = "https://book.douban.com/"
data = requests.get(url).text
s = etree.HTML(data)


file = s.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/div/div/ul[2]/li[1]')


for div in file:
    name =  div.xpath('./div[2]/div[1]/a/text()')[0]
    url  =  div.xpath('./div[2]/div[1]/a/@href')[0]
    acter = div.xpath('.//div[2]/div[2]/text()')[0]

print("{}--->{}--->{}".format(name,url,acter))