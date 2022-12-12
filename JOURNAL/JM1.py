import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="emp")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
ans="y"
c=0
while ans=="Y" or ans=="y":
    c+=1
    empno=int(input("enter employeee number"))
    name=input("enter name of employee")
    des=input("enter designation of employee")
    dep=input("enter department number of employee")
    sal=int(input("enter salary of employee"))
    cursor.execute('Insert into emp1 values({},"{}","{}","{}",{})'.format(empno,name,des,dep,sal))
    mycon.commit()
    ans=input("want to enter another record (y/n)")
print("successfully entered ",c,"records")
mycon.close()
