
x=list(int(input('enter a matrix')))
y=list(int(input('enter a matrix')))
r=[]
for i in range(len(x)):
    for j in range(len(x[i])):
        r[i][j]=x[i][j]+y[i][j]
print(r)
