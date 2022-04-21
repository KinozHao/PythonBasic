# 面向对象在python中的体现
"""
类 有属性和行为
人   是类
枪   是类  种类
子弹 是类   型号
配件 是类   类型
皮肤 是类   系列
背板 是类   容器
药   是类  用途
载具 是类   形式

"""

# 保护对象的属性
class Person(object):
    # 定义名字
    def __init__(self,name):
        # 私有(保护)变量__两个下划线
        self.__name = name
    def getName(self):

        return self.__name
    def setame(self,newName):
        if len(newName) >=5:
            self.__name = newName
        else:
            print("error:名字长度大于等与5")

# 创建对象
duixiang = Person("Kinoz")
print(duixiang.getName())

duixiang.setame("JackMa")
print(duixiang.getName())


# python中没有c++中的public private 这些关键词来区分共有属性和私有属性
# 它是以属性命名的方式来区分的 如果再属性名前面加两个下划线__则表明该属性是私有属性
# 否则就是公众属性

