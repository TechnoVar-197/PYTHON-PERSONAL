a = "y"
x = open("upper.txt",'w')
y = open("lower.txt",'w')
z = open("other.txt",'w')
while a=="y" or a=="Y":
    b = input("enter a character")
    if b.isupper():
        x.write(b)
    elif b.islower():
        y.write(b)
    else:
        z.write(b)
    a = input("want enter another character (y/n)")

print("successfully writen character(s) in a file")
