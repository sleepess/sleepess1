class AgeException(Exception):
    def __init__(self,age):
        self.age = age

class Person:
    i = 0
    def bigandsimle(self,age):
        while True:
            if age >= Person.i:
                print(age)
                break
            else:
                raise ("小于0")


p = Person()
try:
    b = int(input("请输入："))
    p.bigandsimle(b)
except:
    raise AgeException("不是数字")


class moneybig(Exception):
    def __init__(self,money):
        self.money = money

ye = 3000
try:
    money = int(input("输入钱："))
    if money > ye:
        raise moneybig("余额不足")
    else:
        print(ye-money)
except ValueError:
    print("输入错误")




