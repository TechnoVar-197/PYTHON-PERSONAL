def check(x,y):
    x+=".csv"
    y+=".csv"
    import csv
    f=open(x,"r")
    wy=csv.reader(f)
    ch=""
    with open(y,"w",newline="") as h:
        rx=csv.writer(h,delimiter="|")
        for i in wy:
            rx.writerow(["Check"]+i)
    f.close()
    print("file create with new delimiter")

x=input("enter name of file of delimitor is to be changed")
y=input("enter name of to be created with new delimitor")
check(x,y)
