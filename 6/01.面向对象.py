"""
stu_a = {
    "name":"Jack",
    "age":21,
    "gender":1,
    "hometown":"ZheJiang",
}

stu_b = {
    "name":"Sunny",
    "age":22,
    "gender":2,
    "hometown":"BeiJing",
}

stu_c = {
    "name":"Tom",
    "age":19,
    "gender":1,
    "hometown":"Shanghai",
}
# python既有面向对象 又有面向过程
def stu_infor(stu):

    for key,value in stu.items():
        print(key,"=",value)
stu_infor(stu_a)
"""

# 面向过程
# 1 网上查阅资料
# 2 您所需求的带和你的预算得匹配
# 3 根据我们所需的配置然后去实体店询问 无法辨别实用性 然后瞎找了一家
# 4 听他吹牛逼 心动 买
# 5 砍价  6成交

"""
面向对象:
1 找个懂行的人 让他帮你买
2 给钱交易
"""

"""
面向过程
1 养鸭子
2 鸭子养成
3 杀鸭
4 拔毛
5 腌制酱料
6 准备啤酒
7 烹饪
8 装盘,吃
9 卒
面向对象:
1 找家饭店
2 交易
3 吃
4 胖6斤
"""
"""
面向过程
强调的是步骤,过程,带自己去实现

面向对象:
对于我们来说,不必亲自的实现整个步骤,只要调用最方便的事物或是人就可以解决问题
至今没有统一的概念 定义为: 按我们认识客观世界的系统思维方式
采用基于对象(实体),的概念建立的模拟客观世界分析 设计 实现软件的方法
"""

"""
# 类和对象
class car:
    luntai = 4
    color = "Red"

    def getCar(self):
        print("雷克萨斯车子轮胎个数: %d,颜色是: %s"%(self.luntai,self.color))
# car().getCar()

lkss = car()
lkss.getCar()

# 定义类有两种 新式类和经典类 上面的car经典类 car()新式类
# 类命名的规则: 大驼峰
class Choose:
    def skill(self):
        print("using")
    def move(self):
        print("hero moveing")
    def dance(self):
        print("hero danceing")

LOL = Choose()
LOL.skill()
LOL.move()
LOL.dance()
# 添加属性
LOL.attack = "attack"
LOL.length = 13


print(id(LOL.attack))
print(id(LOL.length))
#打印函数是地址池
print(LOL.dance)
#打印地址
print(LOL)


# 类的内置函数(魔法方法)
class Hero:     #经典类
    #在创建完对象之后,会自动调用,它是完成对象的初始化功能

    #初始化变量(魔法方法)
    def __init__(self):
        self.skillnum = 4
        self.color = "red"
        self.name ="Katlina"
    def attact(self):
        print("Your hero's name: %s is attack the target!"%(self.name))

SuperMan = Hero()
print("Hero's color is: %s"%(SuperMan.color))
SuperMan.attact()

class student:
    #初始化变量(魔法方法)
    def __init__(self,name,age,gender,hometown,):
        self.name = name
        self.age = age
        self.gender = gender
        self.hometown = hometown
    def input(self):
        print("Name:%s"%(self.name))
        print("Age:%s"%(self.age))
        print("gender:%s"%(self.gender))
        print("hometown:%s"%(self.hometown))

# 创建对象
xs = student('Kinoz','2','Male','Yiwu');     # 添加内容

xs.input()
"""

# 魔法方法二
"""
颜色 品牌 型号

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
"""


# slef
# 理解self  相当于java中 this和super的结合
class Animal:
    def __init__(self,name):
        self.name = name
    def PrintName(self):
        print("Name : %s"%(self.name))

def myPrint(Animal):
    Animal.PrintName()

dog = Animal("Dogi")
dog.PrintName()

cat = Animal("MiaMi")
myPrint(cat)

# 打印地址
address = id(dog)
address1 = id(cat)
# 打印地址是 10进制
print(address)
print(address1)
print("16进制: %x"%(address))