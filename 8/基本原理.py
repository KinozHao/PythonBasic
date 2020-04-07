# 爬虫就是 所谓请求  网站并提取 数据的 自动化 程序

# 爬虫的流程 (分为四个步骤)
# 1. 发起请求
# 通过http库向目标站点发起请求,及发送一个request 请求可以包含额外的headers等信息,等待服务器的响应。

# 2. 获取相应的内容
# 如果服务器正常响应,会得到一个Response,Response内容便是所要获取的页面内容,类型:二进制,文本,HTML,Json字符串。

# 3. 解析内容
# 得到的内容,可能是HTML可以用正则表达式,网页解析库来进行解析,可能是Json,可以直接为json对象解析,可能是二进制文件

# 4. 保存数据
# 保存的数据多样,可以存为文本,也可以保存到数据库,或者是保存特定的格式的文件。


# Request
# 1. 请求方式
# import requests
#
# requests.get()
# requests.post()
# 主要的请求方式 就是get和post 还有一些其他的方式: head put delete options ect....
# 请求 url
# url:统一资源定位符,就像一个网页文档,一张图片,一个视频等店铺也是可以用url唯一来确定的
# 请求头
# 包含请求时的头部信息,如User-Agent,Host,Cookies等信息
# 请求体
# 请求时额外携带的数据,如表单提交的是表单数据

# Response
# 响应状态
# 用多重相应状态,如果200表示可以访问(访问成功)
# 301表示跳转 404表示找不到页面 502表示没有网

# 实例
# header 服务器会判断这些信息,判断是否请求合法 解析结果并返回内容
# cookie 缓存机制
import requests
import pprint
response = requests.get("http://www.baidu.com")
responseT = requests.post("http://passport.baidu.com/v2/api/?login")

# 获取网页源代码
# pprint.pprint(response.text)

# 获取网页请求头
print(response.headers)
# 获取网页状态码
print(response.status_code)