import requests
import re



# 获取网站
url = "http://www.xiaohuar.com/list-1-%s.html"

for i in range(4):
    temp = url % i
    response =  requests.get(temp)
    html = response.text

# 请求网站


# 解析网站 获取所有图片
    img = re.findall(r'<img \w+.*="\d+".*?alt="(.*?)".*"(/d/file/\d+/\w+\.jpg)"',html)

    for i in img:
        img_url = i[-1]
        img_name = i[0]

        img_re = requests.get("http://www.xiaohuar.com%s"%(img_url))

        xiaohua = img_re.content

        name = ("http://www.xiaohuar.com%s"%(img_url)).split("/")[-1]
        print(name)
    # 保存数据

        with open("E:\爬虫文件\校花网图片\%s"%(img_name)+".jpg","wb") as f:
            f.write(xiaohua)

