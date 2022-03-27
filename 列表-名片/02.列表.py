
# 列表
"""
list = ["name","skill","where"]

list1 = ["贾科斯","宗师之威","诺克萨斯"]

print(list[0])
print(list1[1])
print(list1[2])

# 列表循环遍历

for i in list1:
    print(i)

length = len(list1)
i = 0
while i < length:
    print(list1[i])
    i += 1
"""

# 列表常见操作

# 添加
"""
list1 = ["贾科斯","宗师之威","诺克萨斯"]

name = input("请添加一个英雄的姓名\n")

# 添加方法
# append方法用于添加到列表的最后
list1.append(name)
print(list1)

# extend可以把另一个列表中的数据逐一添加到这个列表
list2 = ["亚瑟","卡特","大乔"]
list2.extend(list1)
print(list2)    

# insert    在指定位置index前插入元素object
list3 = ["哥布林","小黄毛"]
list3.insert(1,"弓箭手")
print(list3)


# 修改元素
list1 = ["贾科斯","宗师之威",""]
list1[2] = "艾欧尼亚"
print(list1)  

# 查找元素
# index count
PartA = ["A","B","C","D"]
# 左闭右开
print(PartA.index("A",0,2))
print(PartA.count("B"))

# 调用方法时,看清传参值,stop意味着末尾索引不存在

# 删除元素
movie = ["何以为家","复仇者联盟","速度与激情","哪吒"]
print("删除前")

for i in movie:  # 列表的遍历
    print(i)

print("删除后")
# movie.pop()     pop的作用删除最后一个元素    
# print(movie)

movie.remove("速度与激情")   # remove可以删除任意一个元素 无论它在哪一个位置(根据元素的池删除)
print(movie)

# 排序元素
num = [2,5,4546,232,5,32,23]
num.reverse()       # reverse翻转
print(num)

# 在python的基础里面 功能单一的元素 是可以不再去打印的
num.sort()          # sort排序 默认顺序 从小到大 sort不能被赋予变量值

num.sort(reverse=True)  # 里面加上了 reverse就是翻转了

#列表内的元素可以随意移动
"""


# 列表嵌套
schoolName = [["浙大","财大","人大"]]
print(schoolName)
