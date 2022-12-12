#travel agency
import csv
ty=""
l=["L","S","l","s","sm"]
x="l"
c=0
iu = ["User_ID","Password","User_Type"]
ip = ["Name","Phone_No","Address","User_ID"]
ib = ["Phone_No","Destination","Mode of Travel","Duration"]
rs =["Name",]
while x in l:
    print("L-login")
    print("S-sigup")
    print("E-exit")
    x=input("enter your choice")
    ty=""
    if x=='L' or x=="l":
        usr=input("Enter USER ID")
        paswd=input("Enter PASSWORD")

        uf = open('user.csv','r')
        ur = csv.reader(uf)
        for row in ur:
            if usr == row[0]:
                if paswd == row[1]:
                    ty = row[2]
        print(ty,"MODE")
        pf = open('personal.csv','r')
        pr = csv.reader(pf)
        for row in pr:
            if usr == row[3]:
                pi = row[1]
        if ty == "admin" or ty == "Admin" :
            y=[1,2,3,4,5,7,8,9]
            sm=1
            while sm in y:
                print("1- View client details")
                print("2-View/search of details of STAY")
                print("3-Modify details of a client")
                print("7-LOGOUT")
                print("8- EXIT")
                sm=int(input("enter your choice"))
                if sm == 1:
                    res = []
                    ui = input("enter phone number of client")
                    bf = open('personal.csv','r')
                    br = csv.reader(bf)
                    for row in br:
                        if ph == row[1]:
                            res = row
                            print(res)
                if sm == 2:
                    bi = int(input("enter phone number to view details of stay "))
                    bf = open('booking.csv','r')
                    br = csv.reader(bf)
                    res = []
                    for row in br:
                        if ph == row[1]:
                            res = row
                            print(res)
                if sm == 3:
                    bi = int(input("enter phone number to modify  details"))
                    ui = input("enter phone number of client")
                    bf = open('personal.csv','a')
                    br = csv.reader(bf)
                    res = []
                    nre = []
                    for row in br:
                        if ph == row[1]:
                            res = row
                            nre = row
                            print(res)
                            print("enter details to be changed")
                            print("1.name")
                            print("2.address")
                            ch = int(input("enter choice:--"))
                            if ch == 1:
                                na = input("enter new name")
                                nre[0] = na
                            elif ch == 2:
                                ad = input("enter new address")
                                nre[2] = ad
                            row = nre
                    print("records updated")
                if sm == 7:
                    sm = 0
                    x = "l"
                if sm == 8:
                    x = "k"
                    sm = 0

        elif ty == "client" or ty == "Client":
            y = [1, 2, 3, 4, 5,]
            sm = 1
            res = []
            while sm in y:
                print("1-add new booking")
                print("2-view booking details")
                print("4-Logout")
                print("5-exit")
                sm = int(input("enter your choice"))
                if sm == 1:
                    de = input("enter destinaton")
                    mt = input("enter mode of travel")
                    du = input("enter duration of stay in number of days")
                    dat = [pi,de,mt,du]
                    bf = open('booking.csv','a')
                    bw = csv.writer(bf)
                    bw.writerow(dat)
                    bf.close()
                    print("YOUR IS BOOKING IS ENTERED IN OUR SYSTEM")
                if sm == 2:
                    ph = int(input("enter phone number to view booking details"))
                    bf = open('booking.csv','r')
                    br = csv.reader(bf)
                    for row in br:
                        if ph == row[0]:
                            res = row
                            print(res)
                    bf.close()
                if sm == 4:
                    sm = 0
                    x = "l"
                if sm == 5:
                    x = "k"
                    sm = 0

        
    elif x=="s" or x=="S":
        print("PLEASE CREATE A NEW ACCOUNT")
        print("PLEASE ENTER FOLLOWING DETAILS")
        nam=input("enter your name")
        ph=int(input("enter your phone number"))
        ad=input("enter your address (max 100 characters)")
        us=input("enter user id")
        pa=input("enter password")

        uh = open('user.csv','a')
        ur = csv.writer(uh)
        ph = open('personal.csv','a')
        pr = csv.writer(ph)
        du = [us,pa,"Client"]
        dp = [nam,ph,ad,us]
        pr.writerow(dp)
        ur.writerow(du)
        uh.close()
        ph.close()
        print("YOU HAVE CREATED THE ACCOUNT")
        print("PLEASE LOGIN WITH YOUR USER ID AND PASSWORD ENTER ABOVE")
        x="l"
    elif x == "e" or x == "E":
        print("EXITING CODE.....")
        print("CODE WRITTEN BY DEV MISHRA")
        print("EXIT")
    else:
        print("PLEASE SELECT CORRECT OPTION")
        ty = "sm"
