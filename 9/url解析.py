# url解析(urlparse)（链接解析）(理解即可)

from urllib.parse import urlparse

result = urlparse("https://www.bilibili.com/video/av63821554/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.18")
print(type(result),result)

# 选择协议
result1 = urlparse("bilibili.com/video/av63821554/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.18",scheme='http',)
print(result1)

