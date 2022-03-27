import random       #导包
# 初始化
bgs = [[],[],[]]     # 三个办公室

teacher = ["1","2","3","4","5","6","7","8",]   # 八位老师

# 初始化变量
i = 1

# 遍历老师的列表(调用随机方法)
for name in teacher:
    index = random.randint(0,2)

    bgs[index].append(name)     # 随机某一个office添加遍历好的老师

    # 当前办公室现有的老师
for tempName in bgs:            # 哪些老师到了哪些办公室
    print("办公室%d的人数为%d"%(i,len(tempName)))      # len获得每个办公室的索引
    i += 1                                           # 自增 获取下一个办公室

    # 当前办公室老师的名字
    for name in tempName:
        print("%s"%(name),end="")
        print(" ")
        print("-"*6)