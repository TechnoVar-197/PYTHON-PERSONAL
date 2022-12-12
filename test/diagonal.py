r=int(input("enter the number of rows "))
c=int(input("enter the number of columns "))
x=[]
print('enter the entries rowwise')
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input())
    x.append(a)
for i in range(r):
    for j in range(c):
        print(x[i][j],end=" ")
    print()
p=[]
s=[]
if r==c:
    for i in range(0, c):
        for j in range(0, c):
            if (i == j):
                p += x[i][j]
            if ((i + j) == (n - 1)):
                s += x[i][j]  
print("Principal Diagonal:", p) 
print("Secondary Diagonal:", s) 
