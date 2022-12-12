import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="project")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
elif mycon.is_connected()==True:
    print("TRAVEL AGENGY")
cur=mycon.cursor()
usr=input("enter")
cur.execute("select (booking_ID) from booking")
data = cur.fetchall()
bi = 0
p=0
c=0
for i in data:
    c += 1
    if c == (len(data)):
             te = i
             bi = te[0] + 1
             print("BOOKING ID:-",bi)
cur.execute("select (phone_no) from client where user_id='{}'".format(usr))
data=cur.fetchone()
ph=0
for i in data:
             p=i
             print(p)
