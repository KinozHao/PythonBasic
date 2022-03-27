# class father(object):
#     def __init__(self,name,color="white"):
#         self.name = name
#         self.color = color
#     def run(self):
#         print("%s keep running"%(self.name))
#
#
# class son(father):
#     def setName(self,newname):
#         self.newname = newname
#     def eat(self):
#         print("%s is eating"%(self.name))
#
# sons = son("Lee")
# print("son's name : %s"%(sons.name))
# print("son's color : %s"%(sons.color))
# sons.eat()
# sons.setName("LastSon")
# sons.run()

# 访问私有属性
class Animal(object):
    def __init__(self,name="Animal",color="Pink"):
        self.__name = name
        self.color= color
    def __text(self):
        print(self.__name)
        print(self.color)

    def text(self):
        print(self.__name)
        print(self.color)

class tiger(Animal):
        def tigerText1(self):
            print(self.__name)
            print(self.color)

Tongwu = Animal()
# program get bug can't view the private element
# absalule know your are my son can't get the information
# Tongwu.__text()
print("Animals color:",Tongwu.color)
Tongwu.text()


# Tig = tiger(name='PinkTiger',color='pink')
# Tig.tigerText1()