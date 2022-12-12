import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="student")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
cursor.execute("select * from student1;")
data=cursor.fetchone()
count=cursor.rowcount
print("total no of rows retviveed in resultsheet",count)
print(data)
data=cursor.fetchone()
count=cursor.rowcount
print("again fetching another record",count)
print(data)
data=cursor.fetchone()
count=cursor.rowcount
print("again fetching another record",count)
print(data)
