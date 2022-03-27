import operator
from operator import *

# eq比较内容是否相同
print(operator.eq("理工男","文科女"))


z = 1
f = 5
"""
lt<     le<= 
eq==    ge>=    gt>
"""
for func in (lt,le,eq,ge,gt):
    print(func(z,f),end="")


# 多维列表
some = [(2,3),(4,5)]
print(some[0])          #获取第一个列表
print(some[1][0])       #获取到4