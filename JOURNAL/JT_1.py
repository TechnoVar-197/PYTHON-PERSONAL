#write a program to get student data from user
# as long as user wants to add more
# and write into a binary file
import pickle
stu = {}
stufile = open("stud.dat","wb")
ans = "y"
c = 0
while ans=="y" or ans=="Y":
    c+=1
    rno = int(input("enter rollnumber of student"))
    name = input("enter name of student")
    marks = int(input("enter marks of student"))

    stu["rollno"] = rno
    stu["name"] = name
    stu["marks"] = marks
    pickle.dump(stu,stufile)
    ans = input("want another (y/n)")
print("successfully written ", c , "records")
stufile.close()

