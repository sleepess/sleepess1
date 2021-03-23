from view import View
from user import User
from address import Address
from bank import Bank
import random
# 开户逻辑
def addUser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0,9)]  # 拼接

    account = string
    print("账号为：",account)
    username = input("请输入姓名：")
    password  = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))

    add = Address()
    add.setCountry(country)
    add.setProvince(province)
    add.setStreet(street)
    add.setDoor(door)

    u =  User()
    u.setAccount(account)
    u.setUsername(username)
    u.setPassword(password)
    u.setMoney(money)
    u.setAddress(add)


    # 调用银行的开户方法
    s = Bank().bank_AddUser(u)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：",account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("******************开户行地址：", Bank().bankName)

    elif s == 2:
        print("该用户已存在！")
    elif s ==  3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")

while True:  # 一直循环的进入选项
    View().printWelcome()
    chose = input("请输入您的选项：")
    if chose == "1": # 判断是否是1
        addUser()
    elif chose == "2": # 判断是否是2
        print("存款！")
    elif chose == "3":  # 判断是否是3
        Bank().bank_gmoney()
    elif chose == "4":  # 判断输入的是否是4
        print("转账")
    elif chose == "5": # 判断输入的是否是5
        print("查询账户！")
    elif chose == "6":   # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")
















