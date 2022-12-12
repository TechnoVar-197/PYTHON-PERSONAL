#create a hold some data
f = open("new.txt","w")
x  = int(input("enter number of records to be entered"))
for i in range(x):
    name = input("enter name students")
    f.write(name)
f.close()
