x=list(int(input('enter a matrix')))
y=list(int(input('enter a matrix')))
r=[]
for i in range(len(x)):
    for j in range(len(y[i])):
        for k in range(len(y)):
            r[i][j]+=x[i][k]*y[k][j]
print(r)
