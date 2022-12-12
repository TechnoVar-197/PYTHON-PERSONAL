f=open("abc.txt",'r')
a=f.read()
fd={}
w=a.split()
m=0
mw=""
for i in w:
    c=a.count(i)
    fd.update({i:c})
    if c>m:
        m=c
        mw=i
print("most occuring word is ",mw)
print("Number of times it occured is:",m)
