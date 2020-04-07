import re

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

result1 = re.search('<li.*?active.*?singer"(.*?)">(.*?)</a>',html,re.S)
if result1:
    print(result1.group(1),result1.group(2))

print("*"*100)

# re.findall 搜集字符串,以列表形式返回全部能匹配的字符串
result2 = re.findall('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result2)
for v in result2:
    print(v)
