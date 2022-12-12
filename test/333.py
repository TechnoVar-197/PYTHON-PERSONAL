def fac(n):
    if n > 0:
        fac(n-2)
        return n*(n-1)
    elif n==0:
        return 1
x = int(input("enter a number"))
a = fac(x)
print(a)
