import pickle
stud = {}
stufile = open ("stud.dat","rb")
try:
    print("file stud.dat holds following records")
    while True:
        stud = pickle.load(stufile)
        print(stud)
except EOFError:
    stufile.close()