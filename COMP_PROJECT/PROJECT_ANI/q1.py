#Made by Aniruddha Ponnuri
#Roll No.-17630436
import pickle
stu = {}
i = 0
stufile = open("stu.dat","wb")
ans = "y"
while ans == 'Y' or ans == 'y':
    rn = int(input("Enter RollNo:--"))
    nm = input("Enter Name:--")
    stu["RollNo."] = rn
    stu["Name"] = nm
    pickle.dump(stu,stufile)
    ans = input("want to enter another record (Y/N)")
    i+=1
print("Successfully entered",i,"records")
stufile.close()
