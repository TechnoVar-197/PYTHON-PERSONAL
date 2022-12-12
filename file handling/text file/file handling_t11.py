# read a text file line by line
# and display each word separated by "#"
f = open("abc.txt","r")
line = " "
while line:
    line = f.readline()
    for word in line.spilt():
        print(word , end = "#")
    print()
f.close()
