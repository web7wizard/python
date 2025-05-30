import mysql.connector
conn=mysql.connector.connect(user="root",passwd="jiya1234")
#print(conn)
cursor=conn.cursor()
cursor.execute("create database my database")
print("created successfully")

conn.close()
