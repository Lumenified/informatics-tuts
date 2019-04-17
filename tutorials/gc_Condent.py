

def my_seq(*myfile):
    """
    this function calculates the amount of Guanine and Cytosine contents
    """
    with open(str(myfile[0]), "rU") as f:
        return f.readlines()[1:]
        
seq = my_seq("../Drosophila melanogaster chromosome 3R.fasta")

print(seq)