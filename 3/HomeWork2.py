# coding:utf-8

# 1. 打印功能提示
print("=" * 50)
print("   名片管理系统   ")
print(" 1. 添加一个新的名片")
print(" 2. 删除一个名片")
print(" 3. 修改一个名片")
print(" 4. 查询一个名片")
print(" 5. 显示所有的名片")
print(" 6. 退出系统")
print("=" * 50)

# 用来存储名片
card_infors = []

while True:

    # 2. 获取用户的输入
    num = int(input("请输入操作序号:"))

    # 3. 根据用户的数据执行相应的功能
    if num == 1:
        new_name = input("请输入新的名字:")
        new_qq = input("请输入新的QQ:")
        new_weixin = input("请输入新的微信:")
        new_addr = input("请输入新的住址:")

        # 定义一个新的字典,用来存储一个新的名片
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['qq'] = new_qq
        new_infor['weixin'] = new_weixin
        new_infor['addr'] = new_addr
        # 将一个字典,添加到列表中
        card_infors.append(new_infor)

        # print(card_infors)# for test

    elif num == 2:
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
    elif num == 3:
        modify_name = input("请输入要修改的人的姓名：")  # 输入要修改的那个人的姓名
        find_flag = 0  # 默认表示没有找到
        modify_flag = 0  # 判断是否修改成功，默认修改失败
        sign = 0
        for temp in card_infors:
            sign += 1
            if modify_name == temp["name"]:
                find_flag = 1 # 找到了
                print("1.修改姓名")  # 打印修改菜单
                print("2.修改QQ")
                print("3.修改weixin")
                print("4.修改地址")
                print("5.退出修改系统")
                while True:
                    num2 = int(input("请输入你要修改的信息的编号："))  # 输入修改项对应的编号
                    # 多维列表
                    if num2 == 1:
                        card_infors[sign - 1]["name"] = input("请输入您要修改的正确姓名：")  # 在对应的修改编号下修改相应的信息
                        modify_flag = 1 # 改好了
                    elif num2 == 2:
                        card_infors[sign - 1]["qq"] = int(input("请输入您要修改的正确QQ："))
                        modify_flag = 1
                    elif num2 == 3:
                        card_infors[sign - 1]["weixin"] = int(input("请输入您要修改的正确weixin："))
                        modify_flag = 1
                    elif num2 == 4:
                        card_infors[sign - 1]["addr"] = input("请输入您要修改的正确地址：")
                        modify_flag = 1
                    elif num2 == 5:
                        break
                    else:
                        print("输入有误，请重新输入:")
                    if modify_flag == 1:  # 判断是否修改成功
                        print("修改成功！")
                        break
                break
    elif num == 4:

        find_name = input("请输入要查找的姓名:")
# [{"name":"","QQ":""}]
        find_flag = 0  # 默认表示没有找到

        for temp in card_infors:
            if find_name == temp["name"]:
                print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
                find_flag = 1  # 表示找到了
                break

        # 判断是否找到了
        if find_flag == 0:
            print("查无此人....")
    elif num == 5:
        print("姓名   \t  QQ  \t      微信      \t      住址")
        for temp in card_infors:
            print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
    elif num == 6:
        break
    else:
        print("输入有误,请重新输入")

    print("")
