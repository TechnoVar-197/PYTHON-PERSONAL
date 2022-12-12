#display size of file after removing end of line charater
#i.e. leading and trailing blank spaces
f = open("abc.txt","r")
str = " "
size = 0
tsize = 0
while str:
    str = f.readline()
    tsize += len(str)
    size += len(str.strip())
print("size without leading or trailing sapces",size)
print("totalsize",tsize)
f.close()