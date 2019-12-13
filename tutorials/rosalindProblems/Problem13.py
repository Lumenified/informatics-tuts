f = open("rosalind_iev (2).txt")
myDataSet = []
myData = f.readline()
myInteger = ""
for i in myData:
    try:
        int(i)
        myInteger += i
        #print(i)
    except ValueError:
        myDataSet.append(int(myInteger))
        myInteger = ""
print(myDataSet)
print(((myDataSet[0] + myDataSet[1] + myDataSet[2]) * 2) + (myDataSet[3] * 1.5) + (myDataSet[4]))
