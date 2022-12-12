import random
def ran(n):
    a=10**(n-1)
    b=10**n
    x=random.randrange(a,b)
    print(x)
y=int(input("enter"))
ran(y)
