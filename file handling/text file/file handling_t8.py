#write a programto get roll number names and marks
#of the student of the class and store in a file
count = int(input("enter number of students of the class"))
f = open("name.txt" , "w")
for i in range(count):
    print("enter details for student(s)",(i+1),"below")
    rno = int(input("Roll no."))
    name = input("Name:")
    marks = float(input("marks"))
    rec = str(rno) + ',' + name + "," + str(marks) + "/n"
    f.write(rec)
f.close
