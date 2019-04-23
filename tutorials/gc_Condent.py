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