f = open('name.txt', 'w')
for i in range(5):
    name = input("enter name of student")
    f.write(name)
    f.write("/n")
f.close
