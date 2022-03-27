# del 魔法方法的第三种
# 创建对象后,python的解释器默认调用__init__() 初始化变量,添加一些内容
# 删除一个对象的时候,python的解析器一样默认调用一个方法,这个方法 就是 __del__
import time


class Animal:
    def __init__(self,name):
        print("__init__ method used")
        self.__name = name  #加了下划线 就是私有了
    # When the object was delete it will auto to used
    def __del__(self):
        print("__del__方法被调用")
        print("您创建的对象: %s有误,稍后会删除"%(self.__name))
# Make Object
dog = Animal('Taidi')

# Delete Object
del dog

print("="*30)


cat = Animal("Doors")
cat2 = cat
print("well delete cat object later")
del cat

print("well delete cat2 object later")
del cat2

print("the program will closed 5 mins later")
time.sleep(5)
# 总结
# 当有一个变量保存了对象引用时,此对象的引用计数会+1
# 当使用del删除变量指向对象的时候,如果对象的引用计数不是1,比如3,只会让引用的计数减1
# 当两次调用del的时候,如果再调用1del,是会把对象删除的