import requests

# 请求
File = requests.get("https://cn.bing.com/th?id=OHR.MountFanjing_ZH-CN1999613800_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp")

# 响应
File.encoding="utf-8"
print(File.text)

# 保存文件
with open("D:\Wallpaper\ 49.jpg","wb")as f:
    f.write(File.content)