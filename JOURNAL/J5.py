#Remove all the lines that contain character "a" in a file
#write it to another file
x=open("abc.txt","r")
h=open("xyz.txt","w")
ch=""
c=0
while ch:
    ch=x.readline()
    print(ch)
    z=ch.split()
    print(z)
    if "a" not in z:
        c+=1
        print(ch)
        h.writeline(ch)
        h.flush()
x.close()
h.close()
print("successfully writen lines into file")

        
        
