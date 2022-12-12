x=int(input("enter a number"))
y=int(input("enter a number"))
z=input("enter operator {+ - / ^ x}")
if z=="+":
    a=x+y
    print(a)
elif z=="-":
    a=x-y
    print(a)
elif z=="/":
    a=x/y
    print(a)
elif z=="x":
    a=x*y
    print(a)
else:
    a=x**y
    print(a)