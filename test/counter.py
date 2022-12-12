x=list(int(input('enter a matrix')))
y=int(input("enter the value to be counted"))
c=0
for i in range(len()):
    for j in range(len(x[i])):
        if x[i][j]==y:
            c+=1
print("number of occurences are",c)
