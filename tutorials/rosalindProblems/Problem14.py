import re

def file_opener(filename):
    f = open(filename)
    namelist = []
    sequenceList = []
    myData = f.readlines()
    for i in myData:
        if i[0]==">":
            namelist.append(re.split(r'(>+|\n+)', i)[2])
        else:
            sequenceList.append(re.split(r'(\n+)', i)[0])

    return namelist,sequenceList

mySequences = file_opener("Problem14.txt")
print(mySequences)
