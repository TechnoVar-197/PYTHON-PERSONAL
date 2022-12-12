file=open("email.txt","r")
a=file.read()
max=0
file1_dict={}
max_occuringword=""
word=a.split()
print(word)
for i in word:
    count=a.count(i)
    print(i,count)
    file1_dict.update({i:count})
    if count> max:
        max=count
        max_occuringword=i
    
print("most occuring word is:",max_occuringword)
print("No of times it occured is:", max)



