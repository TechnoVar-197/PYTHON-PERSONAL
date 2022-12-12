#Program to read the object eritten in a binary file
# and displsy them
import pickle
emp={}
empfile = open("emp.dat","rb")
c = 0
try:
    while True:
        c+= 1
        emp = pickle.load(empfile)
        print(emp)
except EOFError:
    print("succesfully printed ", c , "records")
    empfile.close()