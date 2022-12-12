import pickle

with open("emp.dat","rb") as f:
    l=pickle.load(f)
    print(l)
f.close
