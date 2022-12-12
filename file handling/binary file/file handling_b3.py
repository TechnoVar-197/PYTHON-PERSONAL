#Program to get student data from user
#and append it into a binary file
import pickle
stu = {}
stufile = open("stud.dat","ab")
ans = "y"
c = 0
while ans=="y" or ans=="Y":
    c+=1
    rno = int(input("enter rollnumber of student"))
    name = input("enter of student")
    marks = int(input("enter marks"))

    stu["rollno"] = rno
    stu["name"] = name
    stu["marks"] = marks
    pickle.dump(stu,stufile)
    ans = input("want another (y/n)")
print("successfully written ", c , "records")
stufile.close
