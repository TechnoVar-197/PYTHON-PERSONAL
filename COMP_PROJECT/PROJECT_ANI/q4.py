#Set-b
#Roll No.-17630436
#Q2
import mysql.connector as mysql

mycon = mysql.connect(host="localhost",user="root",password="0000",database="emp")
if mycon.is_connected() == False:
    print("Error Connecting To MySQL Database")
cur = mycon.cursor()
cur.execute("alter table student1 add contactno varchar(10)")
print("Done")
