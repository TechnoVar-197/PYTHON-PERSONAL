def pr(a,n):
    u = ' '
    b = n
    for i in a:
        if b % 2 == 0:
            t = int(n-1)
            z = u*t
        else:
            t = int((n-1)//2)
            z = u*t
        print(z , i , z , end='')
    print()
def f(n):
    l = [1]
    v = " "
    if n % 2 == 0:
        t = int(n-1)
        h = v*t
        print(h, 1, h)
    else:
        t = int((n - 1) // 2)
        h = v * t
        print(h , 1 , h)
    for i in range(n-1):
        m = [1]
        for j in range(i):
            m.append(l[j]+l[j+1])
        m.append(1)
        l = m
        pr(l,i)
#__main__
x = int(input("enter a nuber"))
print("pascal triangle for ", x ,"is")
f(x)
