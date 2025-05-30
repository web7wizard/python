import mysql.connector 
conn=mysql.connector.connect(user="root",passwd="jiya1234")
csr=conn.cursor()
#sql="create table student(roll int(4),name char(20),per float(5,2))"
#csr.execute(sql)
print("table created")
sql="insert into student values(2501,'jiya',91.88))"
csr.execute(sql)
conn.commit()
print("row inserted")
conn.close()
