#program to display number of lines
f=open("abc.txt","r")
str1 = " "
l = 0
while str1:
    str1=f.readline()
    l+=1
print("number of lines in file",l)
f.close()
