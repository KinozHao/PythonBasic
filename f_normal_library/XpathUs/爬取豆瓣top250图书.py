import requests
import time
from lxml import etree
print("*"*20)
print("豆瓣TOP250图书爬取器V0.01")
print("*"*20)

for i in range(10):
    # 总共10页 用i*25 保证以25为单位递增
    url = "https://book.douban.com/top250?start={}".format(i*25)
    data = requests.get(url).text
    s = etree.HTML(data)
    books = s.xpath('//*[@id="content"]/div/div[1]/div/table')

    for div in books:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        comment = div.xpath('./tr/td[2]/p[2]/span/text()')
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0]

        if len(comment)>0:
            print("{}--->{}--->{}--->{}--->{}".format(title, score,comment,num,href))
        else:
            print("{}--->{}--->{}--->{}".format(title, score,num,href))
        print('\n')


print("以上是豆瓣TOP250的图书")
#  有时候xpath里面有tbody标签 需要手动删除 不然打印出来可能空白
"""
总结一个规律 整本书的xpath和书名和评分的xpath的开始时一样的
//*[@id="content"]/div/div[1]/div/table[1]                            整本书的xpath
//*[@id="content"]/div/div[1]/div/table[1]   /tr/td[2]/div[1]/a          书名的xpath
//*[@id="content"]/div/div[1]/div/table[1]   /tr/td[2]/div[2]/span[2]    评分的xpath
"""