# 灵活又方便的网页解析库,处理高效，支持多种解析器
# 利用它不用编写正则表达式即可方便的实现网页信息的提取

html ='''div id=" songs -list">
<h2 class-"title">
新歌速递
</h2><p class="introduction">
2019新歌排行榜</p>
      <ul id="list" class="list-group"
      <1i data-view="2">心如止水</li>
      <ll data-view "7">
      <a href-"/2.mp3" singer="吴青峰">起风了</a>
      </li>
      <li data-view="4" class-"active">
      <a href="/3.mp3" singer"王贰浪">像鱼</a>
      </li>
      <li data-view"6"><a href="/4.mp3"singer="哥哥">当爱已成往事</a>
      </1i>
      <li data-view-"5">
      <a href="/6.mp" singer="五月天">拥抱</a>
      </li>
      </ul>
      </div>'''

from bs4 import BeautifulSoup
# BeautifulSoup最依赖的解析器
soup = BeautifulSoup(html,"lxml")
"""
# 格式化代码,自动补全代码
print(soup.prettify())
# 打印标签<title>字符串样式
print(soup.title.string)

# 不需要正则表达式
# 标签选择器、
# 输出时附带标签
print(soup.title)
# 当前标签类型
print(type(soup.title))
print(soup.head)
# 如果有多个内容,指挥返回第一条相关内容
print(soup.p)
"""

"""
# 获取标签名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs["class"])
print(soup.p["class"])
# 嵌套选择
print(soup.head.title.string)
"""

# 子节点和子孙节点
# 子节点
print(soup.p.contents)
# 子孙节点
print("-"*30)
for i,child in enumerate(soup.p.children):
    # 函数用于将一个可便利的数据对象(如列表,字典或字符串)组合成一个索引序列,同列数据和数据下标,一般用for循环
    print(i,child)
for a,desc in enumerate(soup.p.descendants):
    print(a,desc)

# 获取父节点


