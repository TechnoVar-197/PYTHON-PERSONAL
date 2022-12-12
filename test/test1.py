def comin(i,j):
    x=str(i)
    y=str(j)
    a=i//(10**(len(x)-1))
    b=j//(10**(len(y)-1))
    if a<b:
        print(x)
    else:
        print(y)
u=int(input("enter"))
v=int(input("enter"))
comin(u,v)
