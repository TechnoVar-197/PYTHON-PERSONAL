#Set-b
#Roll No.-17630436
#Q1

def countrec():
    import pickle
    stu = {}
    found = False
    i = 0
    fb = open('stud1.dat','rb')
    try:
        print("Searching in File .........")
        stu = pickle.load(fb)
        if stu["marks"]>75:
            print(stu)
            found = True
    except EOFError:
        if found == False:
            print("No records in found in the file")
        else:
            print("Successfully found",i,"records")
        fb.close()
          
countrec()
