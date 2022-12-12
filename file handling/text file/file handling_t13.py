#read a text file
#and display the count of vowels and constants in the file
f = open("xyz.txt","r")
ch = " "
vcount = 0
ccount = 0
y = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
x = ['a',"e",'i',"o","u","A","E","I","O","U"]
while ch:
    ch = f.read(1)
    if ch in x:
        vcount+=1
    elif ch in y:
        ccount+=1
print("vowels:",vcount)
print("consonants:",ccount)
f.close()