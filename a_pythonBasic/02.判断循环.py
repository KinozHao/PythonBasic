# if判断语句
# 大学日常
"""
today = input("What's the date:\n")

if today == "Monday":
    print("清晨的阳光 打开手机 回忆过往")
if today == "Tuesday":
    print("今天人工智能的课")
if today == "Wednesday":
    print("今天线性代数的课")
else:
    print("困⛏困⛏")
"""


# if else 语句
"""
corn = 2

if corn == 2:
    print("Bus ok")
else:
    print("More ++")

#elif功能

# 初始化值
num = int(input("输入一个值"))

if  num >=90 and num <= 100:
    print("A")
elif num >=80and num< 90:
    print("B")
elif num >=70 and num< 80:
    print("C")
elif num >=60 and num< 70:
    print("D")
elif num >=0 and num< 60:
    print("不及格")
else:
    print("兄弟你考得什么东西 啥也不会呀")
"""

# 嵌套
SAX = input("YOUR SAX?\n")
GAME = int(input("Game Type\n"))

if SAX == "BOY":        #男生判断的部分
    print("PC GAME")
    if GAME == 1:
        print("WeGame LOL")
elif SAX == "GIRL":     #女生判断的部分
    print("Mobile game")
    if GAME == 2:
        print("PUBG")
else:
    print("学霸")