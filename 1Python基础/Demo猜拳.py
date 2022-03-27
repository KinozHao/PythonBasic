# 猜拳游戏
"""
import random
from....import
random.randint(0,2)
"""

# 电脑的随机值
import random

print("电脑会自动选择,只用确定你自己的即可")

Kinoz = int(input("请输入您本来的 剪刀<1> 石头<2> 布<3>\n"))
Player = random.randint(1,3)

# 测试
print("我自己",Kinoz)
print("电脑:",Player)


# 判断 and 和 or
if(Kinoz==1)and(Player==2)or(Kinoz==2)and(Player==3)or(Kinoz==3)and(Player==1):
    print("恭喜电脑胜利")
elif(Kinoz==1)and(Player==3)or(Kinoz==2)and(Player==1)or(Kinoz==3)and(Player==2):
    print("恭喜玩家胜利")
elif Kinoz==Player:
    print("大家平局")
else:
    print("再来吗")