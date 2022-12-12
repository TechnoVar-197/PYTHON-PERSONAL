import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="emp")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
cursor=mycon.cursor()
cursor.execute("update  emp1 set salary = salary+(salary*0.1)")
print("successfully updated records")
mycon.close()
