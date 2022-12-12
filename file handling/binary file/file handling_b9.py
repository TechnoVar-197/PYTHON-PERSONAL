#search for records with roll no in stud.dat file
# if found display the records
import pickle
stu = {}
found = False
f = open("stud.dat","rb")
searchkeys = []
c = 0
ans = "y"
x = int(input("enter roll number to found in file"))
searchkeys.append(x)
try:
    print("SEARCHING IN FILE STUD.DAT ..........")
    while ans=="y" or ans=="Y":
        stu = pickle.load(f)
        if searchkeys in stu["rollno"] :
            print(stu)
            c+=1
            ans = input("want search more(y/n)")
        elif ans=="y" or ans=="Y":
            x = int(input("enter roll number to found in file"))
            searchkeys.append(x)
            if len(searchkeys)==c:
                found = True
            else:
                found = False
except EOFError :
    if found == False:
        print("no such record in the file")
    else:
        print("search successful")
    f.close()
