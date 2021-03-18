# 确定用户库
import pymysql
con = pymysql.connect(host="127.0.0.1",user="root",password="",database="bank")#连接数据库
youbiao = con.cursor()
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

def getmoney():
    #上面为执行语句，提交到缓存中，需要使用fetchone从提取值进行使用
    while 1:
        i = 0
        getnum = 0
        if chose == "3":
            youbiao.execute("select * from q")
            keys = youbiao.fetchall()
            print(keys)
            account = input("请输入您的账户：")
            if account == "q":
                break
            for g in keys:
                if account in g[0]:
                    while i < 3:
                        youbiao.execute("select pass from q where id = %s",account)
                        password1 = youbiao.fetchall()
                        password1 = password1[0][0]
                        print(password1)
                        password = input("请输入您的密码：")
                        if account == "q":
                            break
                        elif password == password1:
                            print("欢迎回来",account)
                            youbiao.execute("select ye from q where id = %s",account)
                            money = youbiao.fetchone()
                            money = money[0]
                            print("您当前的账户余额为：",money)
                            getnum = int(input("请输入您的取款金额："))
                            if getnum > money:
                                print("您的余额不足，当前余额为：",money)
                                return 3
                            money = money - getnum
                            print("您当前的账户余额为：", money)
                        else:
                            print("密码不正确请重试")
                            i +=1
                            if i == 100:
                                return 2
                else:
                    print("账户不正确，请重试")
                    return 1

while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1": # 判断是否是1
        print("1")
    elif chose == "2": # 判断是否是2
        print("1")
    elif chose == "3":  # 判断是否是3
        getmoney()
    elif chose == "4":  # 判断输入的是否是4
        print("1")
    elif chose == "5": # 判断输入的是否是5
        print("1")
    elif chose == "6":   # 判断输入的是否是6，若是6则需要退出 break
        youbiao.close()
        con.close()
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")