#Made by Aniruddha Ponnuri
#Roll No.-17630436
import pickle
stu = {}
i = 0
stufile = open("stu1.dat","wb")
ans = "y"
while ans == 'Y' or ans == 'y':
    rn = int(input("Enter Admission number:--"))
    nm = input("Enter Name:--")
    pr = int(input("Enter Percentage:--"))
    stu["admission_number"] = rn
    stu["Name"] = nm
    stu["percentage"] = pr
    pickle.dump(stu,stufile)
    ans = input("want to enter another record (Y/N)")
    i+=1
print("Successfully entered",i,"records")
stufile.close()
