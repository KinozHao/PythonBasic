def fozu():
    print("                            _ooOoo_                     ")
    print("                           o8888888o                    ")
    print("                           88  .  88                    ")
    print("                           (| -_- |)                    ")
    print("                            O\\ = /O                    ")
    print("                        ____/`---'\\____                ")
    print("                      .   ' \\| |// `.                  ")
    print("                       / \\||| : |||// \\               ")
    print("                     / _||||| -:- |||||- \\             ")
    print("                       | | \\\\\\ - /// | |             ")
    print("                     | \\_| ''\\---/'' | |              ")
    print("                      \\ .-\\__ `-` ___/-. /            ")
    print("                   ___`. .' /--.--\\ `. . __            ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".         ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |     ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /      ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'====== ")
    print("                            `=---='  ")
    print("                                                        ")
    print("         .............................................  ")
    print("                  佛祖镇楼             BUG辟邪          ")
    print("                  Zen of python:                       ")
    print("                  Beautiful is better than ugly.；      ")
    print("                  Explicit is better than implicit.     ")
    print("                  Simple is better than complex.        ")
    print("                  Complex is better than complicated.   ")
    print("                  Flat is better than nested.           ")
    print("                  Sparse is better than dense.          ")
    print("                  Readability counts.                   ")
    print("                  Now is better than never.             ")
fozu()

def hero():
    print('run')
    print('attack')
    print('skill')
hero()

# 函数的文档说明
def demo(a,b):
    print('The sum: %d'%(a+b))
demo(12,8)

#使用第三方库的时候 我们调用helf是可以看到函数内调用库里的详情

def demo2(a,b):
    c = a+b
    print('DEMO2 The sum: %d'%(c))
demo2(1,2)

# 定义小括号中的参数,用来接收参数用的,成为”形参“
# 调用小括号中的参数,用来传递给函数用的,成为"实参"
# 空参数用来代码设计结构



# 函数的返回值 程序中函数完成一件事之后 最后给调用者的结果
def demo3(a,b):
    return a+b
result = demo3(30,40)
print(result)

"""
a=1
b=2
a,b = b,a
print(a,b)

# a=11 b=55
def text1(a,b):
    a,b = b,a
    print('a:%d,b:%d'%(a,b))
text1(11,55)

"""

# 全局变量 简称:函数外部(整段代码)的变量

a=100;
def text1():
    print(a)

def text2():
    print(a)

text1()
text2()

# 局部变量
def text3():
    global b
    b = 300
    print("text3 b=%d"%(b))