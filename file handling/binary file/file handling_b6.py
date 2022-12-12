#create a file MYFILEINFO and
# write a string having two lines in it
import pickle
string = "this is my file. this is my second line"
with open("myfileinfo.dat","wb") as f:
    pickle.dump(string,f)
print("file succesfully created")
