
x = []
print('enter the entries row wise')
for i in range(r):
    a = []
    for j in range(c):
        num = list(input("enter number for"))
        a.append(num)
        x.append(a)
for u in range(r):
    for v in range(c):
        print(x[u][v], end=" ")
    print()
