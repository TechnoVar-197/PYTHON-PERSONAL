#display the contents of file created
f = open("name.txt","r")
while str:
    str = f.readline()
    print(str)
f.close()