# Cookie(主要用来申明主机登录的状态)
import http.cookiejar,urllib.request

http.cookiejar.CookieJar()

cookie = urllib.request.HTTPCookieProcessor

# 代理(翻墙)
handler = urllib.request.HTTPCookieProcessor(cookie)

# 另辟蹊径去访问网站
opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")

for item in cookie:
    print(item.name+"="+item.value)


filename = "cookie.txt"

# 将cookie传输到咱们创建的文件中
cookie1 = http.cookiejar.MozillaCookieJar(filename)
handler1 = urllib.request.HTTPCookieProcessor(cookie1)

opener1 = urllib.request.build_opener(handler1)
response = opener1.open("http://www.baidu.com")

cookie1.save(ignore_discard=True,ignore_expires=True)

# urllib.request.urlopen()