import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="emp")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
x=input("enter employee no to be deleted ")
cursor.execute("delete from emp1 where Emp_no=()".format(x))
mycon.commit()
print("successfully deleted record")
mycon.close()
