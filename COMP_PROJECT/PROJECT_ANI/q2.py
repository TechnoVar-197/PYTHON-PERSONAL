#Made by Aniruddha Ponnuri
#Roll No.-17630436
import mysql.connector as mysql

mycon = mysql.connect(host="localhost",user="root",password="0000",database="emp")
if mycon.is_connected() == False:
    print("Error Connecting To MySQL Database")
cur = mycon.cursor()
cur.execute("Select * from student1")
data = cursor.fetchall()
count = cur.rowcount()
print("Total",count,"rows retrived")
for row in data:
    print(row)
