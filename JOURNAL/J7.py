l=[]
def insert():
    e=input("enter value to be stacked")
    l.append(e)
    print("successfuly appended value into stack")
    menu()
def delete():
    d=input("enter valued to be deleted:")
    if len(l)<=0:
        print("stack is empty")
    elif len(l)>0:
        if d in l:
            l.remove(d)
            print("successfully removed",d,"from stack")
        elif d not in l:
            print("value entered is not present in stack")
    menu()
def dis():
    if len(l)<=0:
        print("stack is empty")
    elif len(l)>0:
        print("stack contains following value(s)")
        for  i in l:
            print(i)
    menu()
def menu():
    print("1--to insert value into stack")
    print("2--to delete value from stack")
    print("3--to display stack")
    print("4--to exit stack")
    c=int(input("enter number corresponding to your choice"))
    if c==1:
        insert()
    elif c==2:
        delete()
    elif c==3:
        dis()
    elif c==4:
        print("exiting from stack")
    else:
        print('please choose correct option')
        menu()

menu()
