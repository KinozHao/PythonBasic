import requests
from bs4 import BeautifulSoup
import os

mz_url = 'https://www.mzitu.com'


# http请求头
Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
# 此请求头Referer破解盗图链接
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}

# 妹子url发起请求
start_html = requests.get(mz_url,headers=Hostreferer)

# 保存
path = 'E:/mzitu/'

# 获取最大页
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text

same_url = 'https://www.mzitu.com/mm/page'

for n in range(1, int(max_page) + 1):
    # 拼接当前妹子的所有url
    ul = same_url+str(n)

    # 分别对当前类每一页第一次url发起请求
    start_html = requests.get(ul,headers=Hostreferer)

    # 提取所有妹子的标题
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')

    # 遍历所有妹子的标题
    for a in all_a:
        title = a.get_text()
        if(title !=''):
            print("准备开爬: "+title)

            # windows不能创建带?的目录,添加判断逻辑
            if(os.path.exists(path + title.strip().replace('?',''))):
                flag = 1
            else:
                os.makedirs(path + title.strip().repalce('?',''))
                flag = 0

            os.chdir(path + title.strip().replace('?', ''))

            href = a['href']
            html = requests.get(href,headers=Hostreferer)
            mess = BeautifulSoup(html.text,"html.parser")

            pic_max = mess.find_all('span')
            pic_max = pic_max[9].text
            if(flag == 1 and len(os.listdir(path + title.strip().replace('?', ''))) >= int(pic_max)):
                print('已经保存完毕,跳过')
                continue

            for num in range(1, int(pic_max)+1):
                pic = href+'/'+str(num)

                html = requests.get(pic, headers=Hostreferer)
                mess = BeautifulSoup(html.text, "html.parser")
                pic_url = mess.find('img', alt=title)
                print(pic_url['src'])
                html = requests.get(pic_url['src'], headers=Picreferer)

                file_name = pic_url['src'].split(r'/')[-1]

                f = open(file_name, 'wb')
                f.write(html.content)
                f.close()
            print('~~~完成')
    print('第',n,'页完成')
