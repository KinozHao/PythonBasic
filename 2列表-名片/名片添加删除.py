print("**********欢迎进入郝哥的名片管理系统**********")
card_infors = []                            #用来存储名片

def print_menu():
    """完成打印功能菜单"""
    print("="*42)
    print(" 郝老板的名片管理系统")
    print(" 1.添加一个新的名片")
    print(" 2.删除一个名片")
    print("="*42)

def add():
        """完成添加一个新的名片"""
        new_name = input("请输入新的名字：")  # 信息的录入
        new_weixin = int(input("请输入新的微信："))
        new_addr = input("请输入新的住址: ")

        new_infor = {}  # 定义一个新的字典，用来存储一个新的名片
        new_infor['name'] = new_name  # 信息的录入
        new_infor['weixin'] = new_weixin
        new_infor['addr'] = new_addr

        # 将一个字典，添加到列表中
        card_infors.append(new_infor)  # 用append()函数在列表中增加一个字典元素

def dele():
        """用来删除一个名片"""

        dele_name = input("请输入要删除的姓名：")  # 输入要删除的那个人的姓名
        find_flag = 0  # 默认表示没有找到
        for temp in card_infors:
            if dele_name == temp["name"]:
                find_flag = 1  # 表示找到了要删除的人，将find_flag的值修改为1
                card_infors.remove(temp)

                print("删除成功！")  # 用del函数删除该列表中的一个字典元素，如果重名只能删第一个
                break

        if find_flag == 0:
            print("没有您要删除人的信息....")

def main():
    """完成对整个程序的控制"""
    print_menu()                                    #1.打印功能提示

    while True:

        num = int(input("请输入操作序号："))           #2.获取用户的输入

        if num==1:                                  #3.根据用户的数据执行相应的功能
            add()
        elif num==2:
            dele()
        elif num==3:
            break
        else:
            print("输入有误，请重新输入")
        print("")

main()  #调用主函数