# 递归的作用

# 计算阶乘, 1*2*3*4

# 1 找到临界点

def jiecheng(n) :
    # 临界点
    if n == 0 :
        return 1
    else :
        return n * jiecheng(n-1)

print(jiecheng(20))

def jeicheng2(num):
    if num >=1:
        result = num*jeicheng2(num-1)
    else :
        result = 1
    return result

res = jeicheng2(5)
print(res)
