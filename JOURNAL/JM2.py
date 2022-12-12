import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="emp")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
cursor.execute("select * from emp1")
data=cursor.fetchall()
count=cursor.rowcount
print("total number of rows retrived in resultsheet:",count)
for row in data :
    print(data)
mycon.close()
