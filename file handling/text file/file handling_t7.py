#create a file to hold some names separated as lines
#without using write function
f=open("name.txt","w")
x  = int(input("enter number of records to be entered"))
l = []
for i in range(x):
    name = input("enter name students")
    l.append(name+"/n")
f.writelines(l)
f.close()
