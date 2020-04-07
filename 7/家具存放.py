import  pyquery
# 定义一个家类
class home(object):
    # 初始化变量
    def __init__(self,area):
        self.area = area
        self.light = "Lighting"
        self.num = []

    def __str__(self):
        msg = "The home 面积"+str(self.area)
        if len(self.num)>0:
            msg = msg+"存的物品"
            for temp  in self.num:
                msg = msg + temp.getName()+","
            msg = msg.strip(",")
        return msg

    # 容纳物品


# 创建对象
home(180)