"""
# 函数返回值2:
# python可以返回多个返回值
def divid(a,b):
        add = a+b
        cheng = a*b
        return add,cheng

add,cheng = divid(10,9)
print('sum',add)
print('x',cheng)
print("="*30)

# 函数参数2:
# 缺省参数
# 调用函数的时候,缺省函数的值如果没有传入,则被认为是默认值

def demo1(name,age=17):
    print("Name:",name)
    print("Age:",age)

demo1(name="KinozHao")
demo1("autor",20)
print("="*30)
# 注意 带有默认值的参数一定要位于参数列表的最后


# 不定长参数
# 有时可能需要一个函数能处理当初声明是更多的函数,声明是不会被命名

def fnc(a,b,*args,**kwargs): #*是标准调用
    # kwargs是以字典的形式进行展现的    给定义变量传参,是不可以的,不会显示我们想要的值 原理参照short
    # 可变参数演示示列
    print("a:",a)
    print("b:",a)
    print("args:",*args)
    print("kwargs:")

    for key,value in kwargs.items():
        print(key,"=",value)

#fnc(6,8,10,12,m=14,n=16)
print("="*30)

#元组和字典的传参方式
f = (3,4,5)
d = {"m":6,"n":7,"p":8}
fnc(1,2,f,d)

print("="*30)
"""

# 匿名函数
# 用lambda关键词创建小型匿名函数,x
# 这种函数的得名于省略号用def生命函数的标准步骤

sum = lambda arg1,arg2 : arg1+arg2
print("总和为:",sum(1,2))

stu = [
    {"name":"hgb","age":17},
    {"name":"chl","age":18},
    {"name":"gy","age":17},
    {"name":"lb","age":19},
    {"name":"wzx","age":3},
]

#按名字排序
#从左向右看
stu.sort(key=lambda x : x["age"])

print(stu)
