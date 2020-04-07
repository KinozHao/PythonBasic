class SweetPoato:           #SweetPoato后面没有括号 经典类
    #初始化变量
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生"
        self.condiments = []

    def __str__(self,things=input("您要的东西?\n")):

        msg = "您的"+things+"已经处于"+self.cookedString+"的状态"

        if len(self.condiments)>0:
            msg = msg + ",添加的配料为:"
            for temp in self.condiments:
                msg = msg + temp +","
                #去除多余的,符号
            msg = msg.strip(",")
        return msg

    # 进行地瓜的烧烤
    def cook(selfs,time):
        selfs.cookedLevel += time
        if selfs.cookedLevel > 8:
            selfs.cookedString = "烤糊了"
        elif selfs.cookedLevel >5:
            selfs.cookedString = "熟了"
        elif selfs.cookedLevel >3:
            selfs.cookedString = "半生不熟"
        else:
            selfs.cookedString = "还是生的"

    def addCondiments(selfs,temp):
        selfs.condiments.append(temp)

# 创建地瓜对象
digua = SweetPoato()
print(digua)


print("你要的烧烤开始制作了")
print("烤2分钟")
digua.cook(2)
print(digua)

print("又烤2分钟")
digua.cook(2)
print(digua)

print("添加番茄酱")
digua.addCondiments("番茄酱")
print(digua)

print("添加海鲜酱")
digua.addCondiments("海鲜酱")
print(digua)

print("又烤2分钟")
digua.cook(2)
print(digua)

print("您要的地瓜好了 一共是3.5 支付宝还是微信?")