import re

# 匹配目标
content = "Hello 123 4567 World_This is a Regex Demo"

# 不止要匹配全部内容,还要获取到两组数字
result = re.match("Hello\s(\d+)\s(\d+)\sWorld.*Demo$",content)

# 匹配全部内容
print("最终获取表达式:",result)

# 获取两组数字
print("获取两组数字:",result.group(1,2))

content1 = "My name is Kinoz tel:19823420823"

# 先匹配所有内容,再获取单独的电话号码
result1 = re.match("My.*:(\d+)",content1)

print("最终获取表达式1:",result1)
print("获取两组数字1:",result1.group(1))
# 获取范围
print("范围:",result1.span())
print("*"*100)


print("贪婪方式：")
content3 = "Hello 123 4567 World_This is a Regex Demo"
result3 = re.match("H.*(\d+).*o$",content3)
print("最终获取表达式:",result3)
print("获取两组数字:",result3.group(1))
print("*"*100)


print("非贪婪方式：相对获取较少的字符,简称:标准字符")
content4 = "Hello 123 4567 World_This is a Regex Demo"
result4 = re.match("H.*(\d+).*o$",content4)
print("*"*100)

print("转义:")
content5 = "price is $5.55"
result5 = re.match("price is \$5.55",content5)
print("最终获取表达式:",result5)
print("*"*100)


# 总结 尽量使用泛匹配,使用括号得到匹配的目标,尽量使用非贪婪模式,有换行就用re.s

# re.search
# 扫描整个字符串,并返回第一个成功匹配,如果组够多就可以一直返回到组里的内容

content6 = "Extra strings Hello 1234567 Word_This is a Regex Demo Extra strings"
result6 = re.search(".*?(\d+)\s(\d+).*?",content6)
print(result6)