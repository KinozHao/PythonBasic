#coding:utf-8
#导包
import re
import json
import requests
from requests.exceptions import RequestException

#网站访问请求是否成功，不成功抛出异常
def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
#解析当前页面，获取内容

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)

    #yield理解成return 里面有个生成器，当生成一个yield的时候对应的函数就成了一个生成器，生成器的功能就是在yield的区域进行迭代处理
    #在yield的函数是一个生成器，不再是一个函数，这个生成器，有了一个函数，就是next函数，下一步的意思
    #这一次next开始的地方是借着上一次next停止的地方所执行的，所以调用next的时候，生成器并不会从for的函数开始执行，
    # 只是借着上一步停止的地方开始，然后遇到yield后，return要生成的数，此步结束
    for item in items:
        yield {
            "rank":item[0],
            "image":item[1],
            "title":item[2],
            "star":item[3].strip()[3:],
            "time":item[4].strip()[5:],
            "score":item[5]+item[6]
        }
#保存文件
def write_to_file(content):
    #可以存档文件，只读
    with open("pool.txt","a",encoding="utf-8")as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

#在运行之前，分页
#调用已经完成的流程
def main(offset):
    url = "https://maoyan.com/board/4?offset="+str(offset)
    html=get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
