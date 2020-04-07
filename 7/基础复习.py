# 定义一个烤地瓜的类 属性 行为(方法)
class kaodigua:

    # 初始化函数
    def __init__(self):  # 传参内容,几分熟的地瓜 返回熟度范围
        self.cookedLevel = 0
        self.cookedString = "生"
        self.condiments = []

    # 添加配料的方法， __str__()
    def __str__(self):
        msg = self.cookedString + "地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("
            for temp in self.condiments:
                msg = msg + temp + ","
            msg = msg.strip(",")

            msg = msg + ")"
        return msg

    # 添加烤地瓜的方法
    # input() #1-3生的 4-6 半生不熟 7-10熟了 10以上: 烤成灰了
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 10:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 7:
            self.cookedString = "烤好了"
        elif self.cookedLevel > 4:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    # 添加酱料
    def addCondiments(self, condiments):
        self.condiments.append(condiments)


# 进行测试鹿子的好坏
mySweetPotato = kaodigua()
print("------有了一个地瓜，还没有烤-----")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)


print("------接下来要进行烤地瓜了-----")
print("------地瓜已经烤了4分钟-----")
mySweetPotato.cook(4)  # 烤4分钟
print(mySweetPotato)
print("------地瓜又已经烤了3分钟-----")
mySweetPotato.cook(3)  # 又烤了3分钟
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)
print("------地瓜又已经烤了5分钟-----")
mySweetPotato.cook(5)  # 又烤了5分钟
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiments("芥末酱")
print(mySweetPotato)
