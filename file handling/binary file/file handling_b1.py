#write a program to bimary file called emp.dat
#write into it the employee details of some employees avialable
import pickle
emp1 = {"empno":1201,"name":"Anushree","age":25,"salary":45000}
emp2 = {"empno":1211,"name":"Abhishek","age":27,"salary":49000}
emp3 = {"empno":1251,"name":"Ansh","age":29 ,"salary":47000}
emp4 = {"empno":1267,"name":"Alex","age":29,"salary":59000}
empfile = open("emp.dat","wb")
pickle.dump(emp1 , empfile)
pickle.dump(emp2 , empfile)
pickle.dump(emp3 , empfile)
pickle.dump(emp4 , empfile)


print("succcesfully written four dictionaries")
empfile.close()

