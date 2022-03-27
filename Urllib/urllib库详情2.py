import urllib
from urllib import request,parse

# 首先请求连接
url = "http://httpbin.org/post"

# 请求url 请求头
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Host":"httpbin.org",
}

# 如果我想传入一个值给网站
dict = {
    "name":"HelloWord",
}
data = urllib.parse.urlencode(dict).encode("utf-8")
# data参数如果必须要传bytes(字节流)类型,如果是一个字典,先用urllib.parse.urlencode()编码

# 允许传入参数值:
req = urllib.request.Request(url=url,headers=headers,data=data,method="POST")

response = urllib.request.urlopen(req)

html = response.read().decode("utf-8")
print(html)