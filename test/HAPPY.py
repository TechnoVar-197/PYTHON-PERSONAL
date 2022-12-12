def sum_sq_digits(n):
    y=len(str(n))
    a=n
    s=0
    while y>=0:
        s+=(a//(10**y))
        a=a%(10**y)
        y=y-1
    return s
def ishappy(x):
    b=x
    y=sum_sq_digits(b)
    if len(str(y))<=1:
        if y==1:
            print(x,y)
        else:
            print("nat",y)
    else:
        ishappy(y)
x=int(input('enter'))
ishappy(x)