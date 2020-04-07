"""
name = "kinoz"
age = 17
weight = 65.0
print("name %s"%(name))
print("age %d"%(age))
print("weight %f"%(weight))

# 字符串的输入
user = input("enter your name\n")
print("Your name %s"%(user))

password = input("enter your password\n")
print("Your password %s"%(password))


# 下标和切片
name ="yintianxiang"
print(name[::2])  # 扫描整个字符串 按照输入的要求,或许间隔的数值
print(name[:2])   # 直接获取字符串的前两个值
print(name[1:10:2])  # 前两个值是字符串的索引, :后的数值为间隔数

print(name[::-1])   #  反向输出字符串      """

# 常见操作符
# find()        str是否包含在name中 如果是返回开始的索引值 如果不在就不在就会-1
"""
name = "yintianxiang"
print(name.find("tian"))
print(name.find("xia",0,10))


# index         用法和find相同只不过查找内容不在范围里时会报出异常
print(name.index("tian"))
print(name.index("xia",0,10))

# count         入上同样有开始与结束索引值,找到出现在字符串中次数
print(name.count("i"))   """

# replace   替换的意思  参数时 要替换的 新的内容 若有相同内容 添加次数
logo = "I love you ha Ha"
print(logo.replace("ha","Wa Ha",1))

# split     切割 所需切割的次数
print(logo.split(" "))
print(logo.split(" ",2))