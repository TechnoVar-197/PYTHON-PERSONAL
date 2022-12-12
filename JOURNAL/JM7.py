import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="emp")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
deg=input("enter desigation of employee ")
sal=int(input("enter salary of employee"))
cursor.execute("select * from emp1 where designation=() and salary=()".format(deg,sal))
data=cursor.fetchall()
count=cursor.rowcount()
print("successfully fetched ",count,"records")
for i in data:
    print(i)
mycon.close()
