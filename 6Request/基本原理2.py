# 视频爬取 同样是二进制文件 注意保存视频的格式,MP4


# 其他 对于python来说只要能请求到的都嫩获取

# 怎么进行网页解析
# 解析方式
# 1 直接处理
# 2 json解析
# 3 正则表达式
# 4 BeautiSoup
# 5 Pyquery
# 6 X-path

import requests
WB =requests.get("https://m.weibo.cn/")
print(WB.text)