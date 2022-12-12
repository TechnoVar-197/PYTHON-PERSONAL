#create a file to hold some data in separate lines
f=open("name.txt","w")
x  = int(input("enter number of records to be entered"))
for i in range(x):
    name = input("enter name students")
    f.write(name)
f.close()
