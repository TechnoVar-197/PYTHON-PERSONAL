def low(x,y):
    a=(x%10)
    b=(y%10)
    if b<a:
        print("Number having lowest one's digit:",y)
    elif a<b:
        print("Number having lowest one's digit:",x)
    elif b==a:
        print("both numbers have equal one's digit:",a)
m=int(input("enter first number"))
n=int(input("enter second number"))
low(m,n)
