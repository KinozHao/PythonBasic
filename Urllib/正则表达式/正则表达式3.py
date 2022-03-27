import re
# re.sub 替换字符串中的每一个匹配的字符串后返回替换后的字符串

tihuan ="Hello 123 4567 World_This is a Regex Demo"
result = re.sub("\d+","",tihuan)
print(result)

result2 = re.sub("\d+","765 4 321",tihuan)
print(result2)

# match = complie   search finall sub

re.compile()