# 字典 常规操作二

# len()测量字典中,键对值的个数 个数从1开始
dict = {"name":"hao","age":"17"}
print(len(dict))

# keys 返回一个包含字典所有Key的列表
print(dict.keys())
print(dict.values())    #同上获取方法一样

# has_key 如果key在字典中返回true 不在则false
print("name" in dict)
print("id" in dict)

# 遍历
str ="slsh"
for i in str:
    print(i,end=" ")        #end输出在同一行

# 字典遍历
# 遍历字典里的key
print("\n")
for key in dict.keys() :
    print(key)

# 遍历字典里的项
for item in dict.items():
    print(item)

# 同时遍历字典中的key-value值
for key,value in dict.items():
    print("key = %s,value = %s"%(key,value))