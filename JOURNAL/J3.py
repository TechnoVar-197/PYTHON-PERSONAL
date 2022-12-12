import pickle
x=int(input("input roll number"))
r=int(input("enter marks "))
stu={}
found=False
f=open("stud.dat","rb+")
try:
    while True:
        rpos=f.tell()
        stu=pickle.load(f)
        if stu["rollno"]==x:
            y=stu["marks"]
            if len(str(y))==len(str(r)):
                stu["marks"]=r
                f.seek(rpos)
                pickle.dump(stu,f)
                found =True
            else:
                print("marks size doesnot match")
except EOFError:
    if found == False:
        print("No such records in the file")
    else:
        print("Record updated")
    f.close()
