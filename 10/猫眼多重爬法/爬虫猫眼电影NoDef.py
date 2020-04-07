from lxml import etree      # 从lxml中获取关于Xpath的东西
import requests

# 获取网页
url = 'http://maoyan.com/board'
response = requests.get(url)
html = response.text


# 解析网页
s = etree.HTML(html)
# dd[]中用通配符“ * ”代替dd[]中的数字，提取当前页所有电影图片链接的xpath
movie_name_xpath = '//*[@id="app"]/div/div/div/dl/dd[*]/div/div/div[1]/p[1]/a/text()'
# 此处应该看清楚图片的前缀是什么 src可能不行
movie_img_xpath = '//*[@id="app"]/div/div/div/dl/dd[*]/a/img[2]/@data-src'
movie_actor_xpath = '//*[@id="app"]/div/div/div/dl/dd[*]/div/div/div[1]/p[2]/text()'
movie_release_time_xpath = '//*[@id="app"]/div/div/div/dl/dd[*]/div/div/div[1]/p[3]/text()'
movie_score_xpath = '//*[@id="app"]/div/div/div/dl/dd[*]/div/div/div[2]/p/i/text()'

movie_name = s.xpath(movie_name_xpath)
movie_img = s.xpath(movie_img_xpath)
movie_actor = s.xpath(movie_actor_xpath)
movie_score = s.xpath(movie_score_xpath)
movie_release_time = s.xpath(movie_release_time_xpath)


# 最后的输出
# 对 movie_name进行遍历获得每一个节点的详细信息
#  strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for i in range(len(movie_name)):
    print('电影名称：' + movie_name[i])
    print('' + movie_actor[i].strip())  # 这里‘’里没写东西 因为爬取到的text默认带导演两个字 所以说可以不用写
    print('图片链接：' + movie_img[i].strip())
    print('评分：' + movie_score[2 * i] + movie_score[2 * i + 1])
    print(movie_release_time[i])
    print('=' * 110)
