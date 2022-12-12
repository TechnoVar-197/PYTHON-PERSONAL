#flush function
f = open("xyz.txt","w")
f.write("the output is /n")
f.write("my" + "work" + "status" + "is")
f.flush()
s = "ok"
f.write(s)
f.write("/n")
f.write("finally over /n")
f.flush()
f.close()