#read from the file myfileinfo and
# display the string untill letter "o" is encountered
import pickle
string = ""
with open("myfileinfo.dat","rb") as f:
    string = pickle.load(f)
    lst = string.split('o')
    print (lst[0])