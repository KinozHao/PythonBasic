import requests

# 请求百度
# 请求百度照片地址url
File = requests.get("")

# 响应我们握手
# 获取到响应地址的二进制格式
print(File.content)
# 保存文件
with open("E:\pythonimg\d444.png","wb") as f:
    f.write(File.content)


print("您所爬取的文件已经爬取完成:请去根目录进行查看！！")