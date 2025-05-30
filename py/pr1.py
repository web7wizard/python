import mysql.connector as my
con=my.connect(user="root",password="jiya1234",database="employe")
print("connected",con)
csr=con.cursor()
#csr.execute("create database employe")
print("database created")
#sql="create table emp(rollno int(4),name char(10))"
#csr.execute(sql)
print("table created")
sql="insert into emp values(2501,'jiya')"
csr.execute(sql)

sql="insert into emp values(2502,'jk')"
csr.execute(sql)

sql="insert into emp values(2503,'jj')"
csr.execute(sql)
print("three record inserted")


sql="select * from emp"
csr.execute(sql)
rows=csr.fetchall()
for row in rows:
    print(row)

sql="update emp set name='teakook' where rollno=2503"
csr.execute(sql)

sql="select * from emp"

csr.execute(sql)
rows=csr.fetchall()
for row in rows:
    print(row)

sql="delete from emp where rollno=2503"
csr.execute(sql)

sql="select * from emp"

csr.execute(sql)
rows=csr.fetchall()
for row in rows:
    print(row)

con.commit()
con.close()



