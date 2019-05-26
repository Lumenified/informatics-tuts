def my_seq(*myfile):
    """
    this function cleans the blanks between lines
    """
    with open(str(myfile[0]), "rU") as f:
        sequ = f.readlines()[1:]
        myseq = '\n'.join(sequ)
        return myseq.replace("\n", "")
        
def gc_content(*sequence):
        """
        Returns the ratio of Guanine and Cytosine
        """
        i = 0
        for j in range(len(sequence[0])):
                if sequence[0][j] is "G" or sequence[0][j] is "C":
                        i += 1
        mycontentratio = (i/len(sequence[0])) * 100
        return "GC Ratio is: " + str(mycontentratio) + "%"
import time
a = time.time()
SEQ = my_seq("../Drosophila melanogaster chromosome 3R.fasta")
print(gc_content(SEQ))
print(time.time() - a)
import math
def calcGcContent(seq, winSize=100000):
        gcValues = []
        a = len(seq)%winSize
        listnumber = math.floor(len(seq)/winSize)
        for i in range(listnumber):
                subSeq = seq[i*winSize:(i*winSize)+winSize]      
                numGc = subSeq.count('G') + subSeq.count('C')
                value = numGc/float(winSize)
                gcValues.append(value)
                if listnumber == i:
                        subSeq = seq[i*winSize:-1]
                        numGc = subSeq.count('G') + subSeq.count('C')
                        value = numGc/float(a)
                        gcValues.append(value)
        print(len(gcValues))
        print(math.floor(len(seq)/winSize))
        return gcValues
from matplotlib import pyplot
gcResults = calcGcContent(SEQ)
pyplot.title('Drosophila melanogaster GC Content ratio per 100000bp')
pyplot.plot(gcResults, '--bo')
pyplot.show()