import pymysql
host = "localhost"
database="bank"
user="root"
password=""

# 可以处理增，删，改的所有操作
def update(sql,param):
    con = pymysql.connect(host=host,database=database,user=user,password=password)
    cursor = con.cursor()#定义游标
    cursor.execute(sql,param)
    con.commit()  # 提交数据
    cursor.close()
    con.close()

# 可以处理查询所有操作
def select(sql,param,mode="many",size=0):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()  # 提交数据
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()








