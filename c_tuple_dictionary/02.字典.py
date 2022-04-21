
WORD = {"name":"Kinoz",
        "id":"1181",
        "sex":"male",
        "add":"asiacnnj"
        }
"""
print(WORD["name"])
print(WORD["id"])
# 不能用value去调用key 会报KeyError的错误

#  我们不确定字典里面有没有某个键而又想获取他的值,可以使用get方法 还可以设置默认值
age = WORD.get("age",18)    #临时添加一个键对值到字典里面
print(age)
"""

# 字典的常规操作

# 修改元素
new_id = input("enter your new ID: \n")
WORD["id"] = int(new_id)
print("修改后的id是: %d"%(WORD["id"]))
print(WORD)

# 添加元素
new_age = input("enter your age: \n")
WORD["nl"]=int(new_age)
print("添加后的age是: %d"%(WORD["nl"]))
print(WORD)

# 删除元素
# del 删除后不能访问到内容
print("删除之前:%s"%(WORD["id"]))
del WORD["id"]
# print("删除之后:%s"%(WORD["id"]))
print(WORD)


#clear
print("删除之前:%s"%(WORD))
WORD.clear()
print("删除之后:%s"%(WORD))