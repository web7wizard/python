import mysql.connector as my
con=my.connect(user="root", password="jiya1234",database="cmdeptd")
print("Connected",con)
csr=con.cursor()
sql="create table studentdf (roll int(4),name char(20),per float(5,2))"
csr.execute(sql)
print("table created")
sql="insert into studentdf values(2598,'sita',74.89)"
csr.execute(sql)
con.commit()
print("row inserted")
r=2644
n='piya'
p=89
t=(3245,'Sona',78.66)
sql="insert into studentdf values(%s,%s,%s)"
csr.execute(sql,(r,n,p))
con.commit()
csr.execute(sql,t)
con.commit()
print("row inserted")
rows=[(4661,'Gita',78.6),(3213,'Mina',98),(7782,'asha',67.89)]
sql="insert into studentdf values(%s,%s,%s)"
csr.executemany(sql,rows)
con.commit()
print("row inserted")



con.close()
