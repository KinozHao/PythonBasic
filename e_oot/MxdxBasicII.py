'''
类和对象
定义类有两种 新式类:Car()经典类:Car

'''
class Car:
    Tire = 4
    Color = "Red"

    def car_info(self):
        print("This car tire:: %d"%(self.Tire))
        print("This car color: %s"%(self.Color))
#调用自己的方法
Car().car_info()

#实现车的方法
BMW = Car()
BMW.car_info()


print("-------------------------------------------------------")



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
class Hero:   #经典类
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
        print("Name:%s" % (self.name))
        print("Age:%s" % (self.age))
        print("gender:%s" % (self.gender))
        print("hometown:%s" % (self.hometown))

# 创建对象并添加内容
xs = student('Kinoz','2','Male','Yiwu')
# 输出信息
xs.input()