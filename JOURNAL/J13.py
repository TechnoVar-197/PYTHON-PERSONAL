import csv
f=open("student.csv",'w')
sw=csv.writer(f)
sw.writerow(['rollno','name','marks'])
x=int(input("enter no of recordes to be entered"))
for i in range(x):
    print("Record of student",i+1)
    r=int(input("enter rollno"))
    n=input("enter name")
    m=int(input("enter marks"))
    sr=[r,n,m]
    sw.writerow(sr)
f.close()
with open('student.csv','r')as h:
    cr=csv.reader(h)
    for rec in cr:
        print(rec)
    
