
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




'''理解self  相当于java中 this和super的结合'''

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