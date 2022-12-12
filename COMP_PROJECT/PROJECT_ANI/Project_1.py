#travel agency

import mysql.connector as x
mycon=x.connect(host="localhost",user="root",passwd="0000",database="project")
if mycon.is_connected()==False:
    print("error connecting to MY SQL database")
elif mycon.is_connected()==True:
    print("TRAVEL AGENGY")
cur=mycon.cursor()
ty=""
l=["L","S","l","s","sm"]
x="l"
c=0
while x in l:
    print("L-login")
    print("S-sigup")
    print("E-exit")
    x=input("enter your choice")
    ty=""
    if x=='L' or x=="l":
        usr=input("Enter USER ID")
        paswd=input("Enter PASSWORD")
        cur.execute("select Type from user where user_id='{}' and Password ='{}'".format(usr,paswd))
        re=cur.fetchone()
        for i in re:
            ty=i
            print(ty,"MODE")
        if ty == "admin" or ty == "Admin" :
            y=[1,2,3,4,5,6,7,8,9]
            sm=1
            while sm in y:
                print("1- View client details")
                print("2-verify booking details of client")
                print("3-Delete record of client")
                print("4-View/search of details of STAY")
                print("5-View payment details of a client")
                print("6-Modify payment details of a client")
                print("7-LOGOUT")
                print("8- EXIT")
                sm=int(input("enter your choice"))
                if sm == 1:
                    ci = int(input("enter client id of client"))
                    cur.execute("select * from client where client_id={} ".format(ci))
                    data = cur.fetchall()
                    print("client_id,name,Phone_no,Address,user_id")
                    for i in data:
                        print(i)
                if sm == 2:
                    bi = int(input("enter booking id of which status is to be changed"))
                    cur.execute("select * from booking where booking_id={}".format(bi))
                    s=cur.fetchone()
                    print("current status of booking id",bi, "is",s)
                    ch=input("enter new status")
                    cur.execute("update project.booking set status='{}' where booking_id={}".format(ch,bi))
                    mycon.commit()
                    print("records updated")
                if sm == 3:
                    ph=0
                    bi=0
                    ui=0
                    ci = int(input("enter client id to be deleted "))
                    cur.execute ("select phone_no from client where client_id={}".format(ci))
                    p = cur.fetchone()
                    for i in p:
                        ph=i
                    cur.execute ("select user_id from client where client_id={}".format(ci))
                    u = cur.fetchone()
                    for i in u:
                        ui=i
                    cur.execute ("select booking_id from booking where phone_no={}".format(ph))
                    b = cur.fetchone()
                    if b != None:
                        for i in b:
                            bi=i
                        cur.execute("DELETE FROM destination USING destination, booking WHERE `booking`.`Booking_ID` = `destination`.`Booking_ID`AND booking.Booking_ID={}".format(bi))
                        cur.execute("DELETE FROM payment USING payment, booking WHERE `booking`.`Booking_ID` = `payment`.`Booking_Id` AND booking.Booking_ID = {}".format(bi))
                        cur.execute("DELETE FROM booking USING booking WHERE booking.Booking_ID = {};".format(bi))
                        mycon.commit()
                    else:
                        print("No Bookings attached to client ID")
                    cur.execute("DELETE FROM client USING client WHERE client.Phone_No = {}".format(ph))
                    cur.execute("DELETE FROM user USING user WHERE user.user_id = '{}'".format(ui))
                    mycon.commit()
                    print("successfully deleted client records")
                if sm == 4:
                    bi=int(input("enter booking id to view details of stay "))
                    cur.execute("select * from booking,destination where booking.Booking_ID=destinaton.Booking_ID and Booking_ID={}".format(bi))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                if sm == 5:
                    bi=int(input("enter booking id to view details"))
                    cur.execute("select booking_id,payment,payment*tax as 'tax',payment*discount as 'discount',payment + tax - discount as 'total pay' from payment where booking_id={}".format(bi))
                    data = cur.fetchall()
                    for i in data:
                        print(i)
                if sm == 6:
                    bi=int(input("enter booking id to view details"))
                    cur.execute("select payment from payment where 'booking_id'={}".format(bi))
                    py=cur.fetchone()
                    print("current amount to be paid is",py)
                    ri=int(input("enter new amount"))
                    cur.execute("update project.payment set payment='{}' where booking_id={}".format(ri, bi))
                    mycon.commit()
                    print("records updated")
                if sm == 7:
                    sm = 0
                    x = "l"
                if sm == 8:
                    x = "E"
                    sm = 0

        elif ty == "client" or ty == "Client":
            y = [1, 2, 3, 4, 5,]
            sm = 1
            while sm in y:
                print("1-add new booking")
                print("2-delete booking")
                print("3-view payment details")
                print("4-Logout")
                print("5-exit")
                sm = int(input("enter your choice"))
                if sm == 1:
                    cur.execute("select (booking_ID) from booking")
                    data = cur.fetchall()
                    bi = 0
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
                        ph=i
                    de = input("enter destinaton")
                    mt = input("enter mode of travel")
                    ho = input("enter name of hotel")
                    du = input("enter duration of stay in number of days")
                    cur.execute("insert into booking(booking_id,phone_no,destination,mode_of_travel)values({},{},'{}','{}')".format(bi,ph,de,mt))
                    cur.execute("insert into destination(booking_id,hotel,duration) values({},'{}','{}')".format(bi,ho,du))
                    mycon.commit()
                    print("YOUR IS BOOKING IS ENTERED IN OUR SYSTEM")
                if sm == 2:
                    bi = int(input("enter booking no to be deleted "))
                    cur.execute("DELETE FROM destination USING destination, booking WHERE `booking`.`Booking_ID` = `destination`.`Booking_ID`AND booking.Booking_ID={}".format(bi))
                    cur.execute("DELETE FROM payment USING payment, booking WHERE `booking`.`Booking_ID` = `payment`.`Booking_Id` AND booking.Booking_ID = {}".format(bi))
                    cur.execute("DELETE FROM booking USING booking WHERE booking.Booking_ID = {};".format(bi))
                    mycon.commit()
                    print("booking deleted successfully")
                if sm == 3:
                    bi = int(input("enter booking id to view total to be paid"))
                    cur.execute("select * from payment where booking_id={}".format(bi))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                if sm == 4:
                    sm = 0
                    x = "l"
                if sm == 5:
                    x = "E"
                    sm = 0

        
    elif x=="s" or x=="S":
        print("PLEASE CREATE A NEW ACCOUNT")
        print("PLEASE ENTER FOLLOWING DETAILS")
        nam=input("enter your name")
        ph=int(input("enter your phone number"))
        ad=input("enter your address (max 100 characters)")
        us=input("enter user id")
        pa=input("enter password")
        cur.execute("select (client_id) from client")
        data=cur.fetchall()
        ci=0
        for i in data:
            c+=1
            if c == (len(data)):
                te=i
                ci=te[0]+1
        cur.execute("insert into user(user_id,password) values ('{}','{}')".format(us,pa))
        cur.execute("insert into client values({},'{}',{},'{}','{}')".format(ci,nam,ph,ad,us))
        mycon.commit()
        print("YOU HAVE CREATED THE ACCOUNT")
        print("PLEASE LOGIN WITH YOUR USER ID AND PASSWORD ENTER ABOVE")
        x="l"
    elif x == "e" or x == "E":
        print("EXITING CODE.....")
        print("CODE WRITTEN BY ANIRUDDHA PONNURI")
        print("EXIT")
    else:
        print("PLEASE SELECT CORRECT OPTION")
