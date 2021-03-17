# 确定用户库
bank = {"26200213":{"username":"zp","password":"123456","country":"中国","province":"北京","street":"温泉","door":"123","money":30000,"bank_name":"中国工商银行昌平区回龙观支行"},
"11111111":{"username":"zp","password":"123456","country":"中国","province":"北京","street":"温泉","door":"123","money":30000,"bank_name":"中国工商银行昌平区回龙观支行"}
}
# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info = '''
    *********************************
    *    中国工商银行账户管理系统     *
    *********************************
    *   1.开户                      *
    *   2.存款                      *
    *   3.取款                      *
    *   4.转账                      *
    *   5.查询账户                  *
    *   6.Bye！                     *
    ********************************
'''
import random

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    # 判断用户库是否已满
    if len(bank) >= 100:
        return 3

    # 判断是否存在
    # 获取所有键，然后在判断是否有
    keys = bank.keys()
    if account in keys:
        return 2
    # 正常开户
    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

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
    # 调用银行的开户方法
    s = bank_addUser(account,username,password,country,province,street,door,money)

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
        print("******************开户行地址：", bank_name)

    elif s == 2:
        print("该用户已存在！")
    elif s ==  3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")

def savemoney():
        i = 0
        savenum = 0
        if chose == "2":
            account = input("请输入您的账户：")
            if account == "q":
                return
            elif account in bank.keys():
                while i < 3:
                    password = input("请输入您的密码：")
                    if account == "q":
                        break
                    elif password == bank[account]["password"]:
                        print("欢迎回来",account)
                        print("您当前的账户余额为：",bank[account]["money"])
                        savenum = int(input("请输入您的存款金额："))
                        bank[account]["money"] = bank[account]["money"] + savenum
                        print("您当前的账户余额为：", bank[account]["money"])
                        break
                    else:
                        print("密码不正确请重试")
                        i +=1
                        if i == 3:
                            break
            else:
                print("账户不正确，请重试")

def getmoney():
    while 1:
        i = 0
        getnum = 0
        if chose == "3":
            account = input("请输入您的账户：")
            if account == "q":
                break
            elif account in bank.keys():
                while i < 3:
                    password = input("请输入您的密码：")
                    if account == "q":
                        break
                    elif password == bank[account]["password"]:
                        print("欢迎回来",account)
                        print("您当前的账户余额为：",bank[account]["money"])
                        getnum = int(input("请输入您的取款金额："))
                        if getnum > bank[account]["money"]:
                            print("您的余额不足，当前余额为：",bank[account]["money"])
                            return 3
                        bank[account]["money"] = bank[account]["money"] - getnum
                        print("您当前的账户余额为：", bank[account]["money"])
                    else:
                        print("密码不正确请重试")
                        i +=1
                        if i == 3:
                            return 2
            else:
                print("账户不正确，请重试")
                return 1

def transfer():
    while 1:
        i = 0
        trmoney = 0
        if chose == "4":
            account = input("请输入您的账户：")
            if account == "q":
                break
            elif account in bank.keys():
                while i < 3:
                    password = input("请输入您的密码：")
                    if password == bank[account]["password"]:
                        getp = input("请输入账号:")
                        if getp in bank.keys():
                            getm = int(input("请输入转账金额:"))
                            bank[account]["money"]=bank[account]["money"]-getm
                            bank[getp]["money"]=bank[getp]["money"]+getm
                            print(bank[account]["money"],bank[getp]["money"])
                            break
                        else:
                            print("转账账号错误请重试")
                    else:
                        print("您的密码错误")
            else:
                print("您的账户名错误")

def serch():
    id = input("请输入您的账号：")
    s = bank.keys()
    if id not in s:
        print("您的账号不存在")
    else:
        password = input("请输入密码")
        if password != bank[id]["password"]:
            print("密码错误请重新输入")
        else:
            print(id)
            print(bank[id]["password"])
            print(bank[id]["money"])
            print(bank[id]["country"])
            print(bank[id]["province"])
            print(bank[id]["street"])
            print(bank[id]["door"])
            print(bank[id]["bank_name"])

while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1": # 判断是否是1
        addUser()
    elif chose == "2": # 判断是否是2
        savemoney()
    elif chose == "3":  # 判断是否是3
        getmoney()
    elif chose == "4":  # 判断输入的是否是4
        transfer()
    elif chose == "5": # 判断输入的是否是5
        serch()
    elif chose == "6":   # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")
