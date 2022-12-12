#program to display size of file in bytes
x = open("abc.txt",'r')
st =  x.read()
s = len(st)
print("size of the given file is",s)
x.close()