"""
a = 0
while a < 10:
    print("我很帅")
    a+=1

# 累加 1+到100
i = 1
sum = 0
while i<=100:
    sum = sum+i
    i += 1
print(sum)

# 嵌套一个直角三角形

i = 1
while i<=5:
    j = 1
    while j<=i:
        print("*",end="")
        j+=1
    print(" ")
    i+=1
"""
# 99乘法表

i = 1
while i<=9:
    j = 1
    while j<=i:
        # print("*",end="")
        sum = i*j         # sum用来存放两个数相乘的值
        print("%d*%d = %d"%(i,j,sum),end=" ")     # 每一个%d代表一个值 类似于C语言
        j+=1
    print(" ")
    i+=1