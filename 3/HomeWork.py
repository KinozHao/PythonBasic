"""
名片管理系统
姓名 QQ 微信 地址
1 实现添加新的名牌你
2 删除一个名片
3 修改一个名片
4 查询一个名片
4 显示所有的名片
5 推出系统
除非点击6 不然一直循环

"""

print("欢迎进入机锋信息录入系统")

card = []           #定义一个列表用来存放名片的信息

def print_menu():           #选择项目
    print("="*20)
    print("<名片管理系统V0.1>")
    print("1: 添加一个新的名片")
    print("2: 删除一个名片")
    print("3: 修改一个名片")
    print("4: 查找一个名片")
    print("5: 显示所有的名片信息")
    print("6: 退出名片管理系统")
    print("="*20)

def add_element():          #add函数用于添加元素
    name = input("输入您的名字: ")
    qq = int(input("输入您的qq号码: "))
    wechat = int(input("输入您的wechat号码: "))
    addes = input("输入您的地址: ")

    infor_dict = {}         # 定义一个字典
    infor_dict['name'] = name   # 把键盘录入的元素存放到字典里面
    infor_dict['qq'] = qq
    infor_dict['wechat'] = wechat
    infor_dict['addes'] = addes

    card.append(infor_dict)     #把字典里的值添加到列表中
    print("添加成功!")


def dele_element():     #dele函数用于删除元素
    dele_name = input("您要删除的姓名:")
    find_flag = 0;      #默认表示没有找到
    for temp in card:
        if dele_name == temp["name"]:   #如果找到了要删除的人 就把find_flag修改为1
            find_flag = 1;
            card.remove(temp)       # 用remove关键词删除字典中的姓名    列表为外围所以remove更好用

            print("删除成功！")       # 做提示
            break

    if find_flag == 0:
        print("没有找到要删除人的信息 ")


def change_element():    #change函数用来修改元素
    change_name = input("您要修改的姓名:")
    find_flag = 0;          # 默认表示没找到
    change_flag = 0;        # 判断修改是否成功 默认0为修改失败
    sign = 0;               # 每次自增1用来逐一查找数据
    for temp in  card:
        sign+=1
        if change_name == temp["name"]:
            find_flag = 1
            print("1:修改姓名")
            print("2:修改QQ")
            print("3:修改微信")
            print("4:修改地址")
            print("5:退出修改系统")
        while True:
            num2 = int(input("请输入您要修改信息的编号"))
            if num2 == 1:
                card[sign-1]["name"] =input("请输入正确的姓名:")    #sign-1意思为 回退
                change_flag = 1
            elif num2 == 2:
                card[sign-1]["name"] =input("请输入正确qq:")
                change_flag = 1
            elif num2 == 3:
                card[sign - 1]["name"] = input("请输入正确wechat:")
                change_flag = 1
            elif num2 == 4:
                card[sign - 1]["name"] = input("请输入正确add:")
                change_flag = 1
            elif num2 == 5:
                print("输入有误 请重新输入")
                if change_flag == 1:
                    print("修改成功")
                    break
        break
def find_element():     #find函数用来查询单个人的信息

    find_name = input("您要查找的名字:")
    find_flag = 0
    print("您要查找的人的信息为：")                    #打印对应姓名的信息
    print("姓名\t\tQQ\t\t\t微信\t\t住址")

    for temp in card:
        if find_name == temp["name"]:
            print("%-8s %-8s %-8s %s"%(temp['name'],temp['qq'],temp['wechat'],temp['addes']))
            find_flag = 1;

    if find_flag == 0:
            print("您查询的人不存在")

def show_all():
    print("姓名\t\tQQ\t\t\t微信\t\t住址")

    for temp in card:       #直接显示出系统中已经存在的信息

            print("%-8s %-8s %-8s %s"%(temp['name'],temp['qq'],temp['wechat'],temp['addes']))



def main():
    print_menu()        #开始要选择的信息
    while True:
        num = int(input("输入你要选择的号码:"))      #对应的数字执行对应的函数

        if num == 1:
            add_element()
        elif num == 2:
            dele_element()
        elif num == 3:
            change_element()
        elif num == 4:
            find_element()
        elif num == 5:
            show_all()
        elif num == 6:
            print("退出系统成功！！！")
            break
        else:
            print("输入有误 重新输入")
        print("")

main()          #调用main函数 实现整个循环体