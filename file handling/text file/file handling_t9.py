#program to add n number of student details in the file created
count = int(input("enter number details of students of the class to be added"))
f = open("name.txt" , "a")
for i in range(count):
    print("enter details for student(s)",(i+1),"below")
    rno = int(input("Roll no."))
    name = input("Name:")
    marks = float(input("marks"))
    rec = str(rno) + ',' + name + "," + str(marks) + "/n"
    f.write(rec)
f.close
