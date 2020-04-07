# 所谓 多态 定义时候类型和运行时的类型不同 此时就是多态

class FAFONE(object):
    def show(self):
        print("FAFONE.show")

class FAFTWO(FAFONE):
    def show(self):
        print("FAFTWO.show")

class FAFTHREE(FAFONE):
    def show(self):
        print("FAFTHREE.show")

def Func(obj):      # obj can us object
    print(obj.show())

FAFONEs = FAFTWO()
Func(FAFONEs)

FAFONEss,FAFONEsss= FAFTHREE()
Func(FAFONEss)

# 鸭子模式 为了让func函数可以执行FAFONEs对象的show方法 又可以执行FAFONEss对象的show方法,所以定义了一个FAFONEs和FAFONEss的父类
# 而真正传入的参数: FAFONEs和FAFONEss的对象