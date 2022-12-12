#check the position of file pointer
# after read function
f = open("abc.txt","r")
print(f.read())
print("file pounter is now at", f.tell())
f.close