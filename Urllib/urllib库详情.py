"""
import pymysql
Me = pymysql.connect(host="localhost",user="root",password="Ytx",port=3306,db="mysql")

# 调用这个方法
cursor = Me.cursor()

# 查询数据库有几条数据
print(cursor.execute('select * from db'))

# 获取当前数据库哦下的所有属性名
print(cursor.fetchone())
"""

# urllib: python内置的http协议请求库
# urllib request 请求模块
# urllib error 异常处理模块
# urllib parse url url解析模块
# urllib robotparser txt解析模块


"""
import urllib.request
import urllib.parse

# anser = urllib.request.urlopen("http://www.oneplus.com")
# #  外部获取的内容,转换成我们能看懂的形式
# print(anser.read().decode("utf-8"))


url = "http://httpbin.org/post"
form = {'user':"Pot","msg":"Hello world"}

data = urllib.parse.urlencode(form)
data = bytes(data,"utf-8")
Rs = urllib.request.urlopen(url,data)
R = Rs.read()
print(R)
"""

"""
# 延时请求 timeout
import urllib.request
import socket
import urllib.error

# url = "http://httpbin.org/get"
# RESPONSE = urllib.request.urlopen(url,timeout=5)
# X = RESPONSE.read()
# print(X)

url = "http://httpbin.org/get"
try:
    RESPONSE = urllib.request.urlopen(url, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("time out")
"""

# 响应
# 响应的类型
import urllib.request

xy = urllib.request.urlopen("http://baidu.com")
print(type(xy))
# 状态码
print(xy.status)

# 获取请求头
print(xy.getheaders())

# 获取请求头的内容
print(xy.getheader("Server"))
