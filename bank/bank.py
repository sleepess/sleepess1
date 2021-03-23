from DBUtils import select
from DBUtils import update
class Bank:
    bankName = "中国工商银行账户管理系统"

    def  bank_AddUser(self,user):
        # 判断数据库是否已满
        sql1 = "select  count(*)  from q"
        data = select(sql1, [])
        if data[0][0] >= 100:  # 如果返回的统计数据超出100，则已满
            return 3
        # 判断数据是否存在改用户
        # 获取所有键，然后在判断是否有
        sql2 = "select * from q  where  id = %s"
        param2 = [user.getAccount()]
        data2 = select(sql2, param2)
        if len(data2) != 0:  # 如果通过sql语句能查到数据并且不为空，则说明改用户已存在
            return 2
        # 正常开户：insert into 表  ，否则则执行存储数据操作
        sql3 = "insert into q values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"  # now() 使用的mysql数据库自己的时间
        param3 = [user.getAccount(),
                  user.getUsername(),
                  user.getPassword(),
                  user.getAddress().getCountry(),
                  user.getAddress().getProvince(),
                  user.getAddress().getStreet(),
                  user.getAddress().getDoor(),
                  user.getMoney(),
                  self.bankName]
        update(sql3, param3)
        return 1

    def bank_gmoney(self):
        account = input("请输入您的账号：")
        passwd = input("请输入您的密码:")
        sql = "select *  from  q  where  id = %s and pass  = %s"
        date = select(sql,[account,passwd])
        if date == ():
            print("输入信息错误")
            return 1
        else:
            sql = "select ye from q where id = %s"
            date = select(sql,account)
            print(date[0][0])
            money = input("请输入修改金额：")
            sql = "update q set ye = ye - %s"
            update(sql,money)
            sql = "select ye from q where id = %s"
            date = select(sql,account)
            if date[0][0] < 0:
                print("您的余额不足")
                sql = "update q set ye = ye + %s"
                update(sql,money)
                sql = "select ye from q where id = %s"
                print(select(sql,account)[0][0])
            else:
                sql = "select ye from q where account = %s"
                print(select(sql,account))

