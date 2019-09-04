# 连接MySQL数据库过程
import pymysql

conn = pymysql.connect('localhost', 'root', 'lyq3163316','xxx')#声明mysql连接对象
cursor=conn.cursor()
sql = """select * from student;"""
# sql = """insert into student (id,name,age) value (9,'dodo',31)"""
print(sql)
try:
    cursor.execute(sql)#执行sql语句
    results = cursor.fetchall()
    for row in results:
        print(row)
    # conn.commit()
except:
    conn.rollback()
conn.close()#关闭链接