import mysql.connector as my
con=my.connect(user="root",password="jiya1234")
print("Connected",con)
csr=con.cursor()
csr.execute("create database cmdeptd")
print("database created")
con.close()

"""
Connected <mysql.connector.connection_cext.CMySQLConnection object at 0x000002557FA27E88>
database created
"""
