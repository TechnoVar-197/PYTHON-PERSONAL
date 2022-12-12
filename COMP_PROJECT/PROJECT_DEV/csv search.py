import csv
def searchname(x):
    ii = input("enter your name")
    file = csv.reader(open('data.csv'))
    for row in file:
        if ii == row[1]:
            x = row
fh = open('personal.csv','w')
fr = csv.writer(fh)
data = [["Name","Phone_No","Address","User_ID"],["Dev Mishra",9911501192,"p5/103",99115]]
fr.writerows(data)
fh.close()
print("success")

