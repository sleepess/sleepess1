num1=1
name1="a"
jiage1=20
pinzhi1="A+"
lexing1="上衣"
xiaoliang1=500

num2=2
name2="b"
jiage2=20
pinzhi2="B+"
lexing2="裤子"
xiaoliang2=300

num3=3
name3="c"
jiage3=20
pinzhi3="A"
lexing3="上衣"
xiaoliang3=200

print("--------------欢迎来到衣服商城系统--------------\n")
print("编号    衣服名称    价格    品质    类型    销量\n")
print(num1,"    ",name1,"    ",jiage1,"    ",pinzhi1,"    ",lexing1,"    ",xiaoliang1)
print(num2,"    ",name2,"    ",jiage2,"    ",pinzhi2,"    ",lexing2,"    ",xiaoliang2)
print(num3,"    ",name3,"    ",jiage3,"    ",pinzhi3,"    ",lexing3,"    ",xiaoliang3)
print("总价=",jiage1*xiaoliang1+jiage2*xiaoliang2+xiaoliang3*jiage3)

'''
    变量：变化存储数据的量
    c = “香蕉”
    c = "苹果"
    print(c)


'''

# 录入第一个水果信息到变量里
id1 = 1
name1 = "苹果"
price1  = 3.9
num1 = 500
quanlity1 = "A+"
Origin1 = "山东"

# 录入第一个水果信息到变量里
id2 = 2
name2 = "香蕉"
price2  = 3.5
num2 = 600
quanlity2 = "B+"
Origin2 = "海南"

print("-----------------------------------------------")
print("-             欢迎来到水果商城系统            -")
print("----------------------------------------------")
print("编号    名称      价格    数量     质量     产地")
print("----------------------------------------------")
print(id1,"     ",name1,"    ",price1,"   ",num1,"   ",quanlity1,"    ",Origin1)
print(id2,"     ",name2,"    ",price2,"   ",num2,"   ",quanlity2,"    ",Origin2)
print("---------------------------------------------")
print("总金额：",(price1 * num1 +  price2 * num2),"￥！")
