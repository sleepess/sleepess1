dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1.请循环遍历出所有Key
print(dict.keys())

#2.请循环遍历除所有的value
k = dict.keys()
for i in k:
    a = dict[i]
    print(a)

#3.请在字典中增加一个键值
dict["k4"]="v4"
print(dict)

#小明去超市购买水果
s = {"苹果":32.8,"香蕉":22,"葡萄":15.5}
while 1:
    a = input("请输入查询名称：")
    if a == "q":
        break
    print(s[a])

s = {"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":15.8}
sum = 0
while 1:
    a = input("请输入购买物品：")
    if a =='q':
        break
    x = int(input("请输入购买数量："))
    b = s[a]
    sum = sum +b*x
print(sum)

#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
def abc(li) :
    a={}
    for i in range(len(li)-1) :
        flag = 0
        for j in range(i):
            if li[j] == li[i]:
                flag = 1
                break
        if flag == 1:
            continue
        if li[i].isdigit():
            counter = li.count(li[i])
            a[li[i]] = counter
        else:
            counter
    return a
a=input("请输入一个列表：")
print(abc(a))

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
name = []
for i in range(len(names)):
    a = names[i][0]
    b = name.append(a)
print(name)
d = dict(zip(name,names))
print(d)
