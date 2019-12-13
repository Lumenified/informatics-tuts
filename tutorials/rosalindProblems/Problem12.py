import re

def file_opener(filename):
    f = open(filename)
    namelist = []
    templist = []
    sequenceList = []
    # print(f.readlines())
    for i in f.readlines():
        #print(i)
        if i[0]=='>':
            namelist.append(re.split(r'(>+|\n+)',i)[2])
        else:
            templist.append(re.split(r'(\n)',i)[0])
    for i in range(len(templist)):
        if i==0:
            pass
        else:
            if len(templist[i])<len(templist[i-1]):
                sequenceList.append(templist[i-1] + templist[i])

    return [namelist, sequenceList]

mylist = file_opener('rosalind_grph.txt')
#print(mylist)
def permer(currentFile, BigONumber):
    perm = []
    for i in range(len(currentFile[1])):
        for j in range(len(currentFile[1])):
            if i==j:
                pass
            else:
                if currentFile[1][i][-BigONumber:]==currentFile[1][j][0:BigONumber]:
                    perm.append([[currentFile[0][i], currentFile[0][j]],[currentFile[1][i], currentFile[1][j]]])
                else:
                    pass
    return perm
mypermList = permer(mylist, 3)
#print(mypermList)

for i in mypermList:
    print(i[0][0] + " " + i[0][1])
