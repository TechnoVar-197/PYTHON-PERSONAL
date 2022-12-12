#standard inpu and uotput devices as file
import sys
f = open("xyz.txt")
l1 = f.readline()
l2 = f.readline()
sys.stdout.write(l1)
sys.stdout.write(l2)
sys.stderr.write("no ERRORS occured")
f.close()

with open("xyz.txt","a") as f:
    f.write("hi there /n")
f.close