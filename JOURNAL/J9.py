#to compare the length of two strings
def com():
    x=input("enter a string")
    y=input("enter another string")
    if len(x)==len(y):
        print("length of both strings are same")
    elif len(x)>len(y):
        print("length of string 1 is greater than string 2")
    elif len(x)<len(y):
        print("length of string 2 is greater than string 1")
com()

