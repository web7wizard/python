import mysql.connector

con = mysql.connector.connect(user="root", password="jiya1234",
                              database="cmdeptd" )


csr=con.cursor()
sql="update student set per=90 where roll=3245"
csr.execute(sql)
con.commit()
print("record updated")


sql="delete from student where name='Gita' "
csr.execute(sql)
con.commit()
print("record deleted")
con.close()

"""
record updated
record deleted
"""
