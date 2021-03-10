#实现输入十个数字，打印结果
b=0
sum=0
while b<10:
    a=int(input("请输入数字:"))
    sum = a+sum
    b+=1
print("数字之和为：",sum)

#从键盘输入十个数，最后打印最大的数，十个数的和，平均数
b=0
sum=0
big=0
while b<10:
    a=int(input("请输入数字:"))
    sum = a+sum
    if a > big:
        big=a
    b+=1
avg=sum/b
print("数字之和为：",sum)
print("最大值：",big)
print("平均数为：" ,avg)

#使用random模块，如何产生50-150之间的数
import random
a=random.randint(50,150)
print(a)

#从键盘输入任意三条边，判断是否能构成三角形，若可以则判断形成什么三角形
a=int(input("第一条边："))
b=int(input("第二条边："))
c=int(input("第三条边："))
if a<=0 or b<=0 or c<=0:
    print("三角形边长不能为0")
elif a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    if a==b==c:
        print("等边三角形")
    elif a==b or b==c or c==a:
        print("等腰三角形")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+b*b==c*c:
        print("直角三角形")
else:
    print("不能构成三角形")

#有以下两个数，用加减号实现两个数的调换
a=78
b=56
print("a=",a-22)
print("b=",b+22)

#实现三次登录验证
c=0
user="root"
password="admin"
while c<3:
    a = input("请输入用户名：")
    b = input("请输入密码：")
    if a==user and b==password:
        print("登录成功")
        break
    else:
        if c == 2:
            print("账户已锁定")
        else:
            print("请确认密码和用户名")
        c+=1

#编程实现图像打印
for i in range(8):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")
    print("")

#使用while循环实现99乘法表
a=1
b=1
while a<=9:
    while b<=a:
        print(a,"*",b,"=",a*b)
        b += 1
    print("\t")
    b=0
    a+=1

#倒叙99乘法表
a=9
b=9
while a>=1:
    while b>=a:
        print(a,"*",b,"=",a*b,end="\t")
        b -= 1
    print()
    b=9
    a-=1

#青蛙爬20米的井
a=3
b=2
c=0
d=0
while 1:
    c=c+a
    if c==20:
        print ("最终天数为：",d)
        break
    c=c-b
    print("目前位置为：",c)
    d+=1
#猜数游戏
import random
import time
gold=0
a = random.randint(1,100)
j = 0
print("您的初始资金为：",gold)
while 1:
    b = int(input("请输入一个数:"))
    if j>20:
        print("好好想一想,休息一下")
        time.sleep(20)
    if j>50:
        print("机会用完了哦,系统锁定")
        while 1:
            time.sleep(1)
    if b > a:
        print("big")
        j+=1
    elif b < a:
        print("simler")
        j+=1
    elif b == a:
        print("yes")
        print("恭喜你在",j,"次完成哦")
        gold=gold+200
        print("你的资金为：",gold)
        break

#循环20的阶乘
a=1
b=1
c=0
while a<20:
    while b<=a:
        print(a," ",b)
        c=c+(a*b)
        b+=1
    b=1
    a+=1
print(c)






