# 魔法方法二

# 颜色 品牌 型号

class cosmetics:
    # 初始化变量
    def __init__(self,newcolor,newtrademark,newmodel):
        self.newcolor = newcolor
        self.newtrademark = newtrademark
        self.newmodel = newmodel

    def __str__(self):
        infor1 = "Color: %s"%(self.newcolor)+"brand: %s"%(self.newtrademark)+"Num: %d"%(self.newmodel)

        return infor1
    def boyfriedn(self):
        print("Wo Beautiful girl")

LV = cosmetics("CherryPink","路易斯",46)
Chanel = cosmetics("Red","香奈儿",20)
Innisfree = cosmetics("Black","Innisfree",216)
print(LV)
print(Chanel)
print(Innisfree)
LV.boyfriedn()
