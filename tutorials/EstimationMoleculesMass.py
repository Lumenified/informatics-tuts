def estimateMolMass(seq, molType='protein'):
    """Calculate the molecular weight of a biological sequence assuming
    normal isotopic ratios and protonation/modification states
    """
    residueMasses = {
    "DNA": {    "A": 331.2218,
    "C": 307.1971,
    "G": 347.2212,
    "T": 322.2085},
    "RNA": {"G":345.21, "C":305.18, "A":329.21, "U":302.16},
    "protein": {"A": 71.07, "R":156.18, "N":114.08, "D":115.08,
                "C":103.10, "Q":128.13, "E":129.11, "G": 57.05,
                "H":137.14, "I":113.15, "L":113.15, "K":128.17,
                "M":131.19, "F":147.17, "P": 97.11, "S": 87.07,
                "T":101.10, "W":186.20, "Y":163.17, "V": 99.13}}
    massDict = residueMasses[molType]
    # Begin with mass of extra end atoms H + OH
    molMass = 0
    i = 0
    for letter in seq:
        molMass += massDict.get(letter, 000.000)

    return float(molMass)
"""proteinSeq = 'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'
"""
""" MY GUESS, BEST GUESS
"""
"""
with open("../kinesin heavy chain [Drosophila melanogaster].fasta", "rU") as f:
    my_seq = f.readlines()[1:]
    seq = ""
    for i in my_seq:
        if i is not " ":
            seq += i
            if len(seq)%100000==0:
                print(len(seq))
        
        #if my_seq.index(i)%1000000==0:
        #   print(my_seq.index(i))

print(estimateMolMass(seq))


from Bio import SeqIO
"""
from Bio.SeqUtils import molecular_weight
"""
my_protein = open("../kinesin heavy chain [Drosophila melanogaster].fasta", "rU")
protein = SeqIO.read(my_protein, 'fasta')
print(estimateMolMass(protein.seq))
"""
from Bio import SeqIO
my_dna = open("../Drosophila melanogaster chromosome 3R.fasta", "rU")
Dnas = SeqIO.read(my_dna, 'fasta')
my_last_dna = ""
import time
print(len(Dnas.seq))
a = time.time()
for i in Dnas.seq:
    if i is 'A':
        my_last_dna += i
    elif i is 'G':
        my_last_dna += i
    elif i is 'C':
        my_last_dna += i
    elif i is 'T':
        my_last_dna += i
    else:
        pass

    """if len(my_last_dna)%1000000 == 0:
        print(len(my_last_dna))
"""
print(time.time() - a)
    
    
MY_LAST_DNA = ''
import time
with open("../Drosophila melanogaster chromosome 3R.fasta", "rU") as f:
    my_seq = f.readlines()[1:]
    seq = '\n'.join(my_seq)
    seq = seq.replace("\n", "")
    MY_LAST_DNA = seq.replace("N", "")
    a = time.time()
    print(molecular_weight(MY_LAST_DNA, seq_type='DNA', monoisotopic=False))
    print(time.time() - a)
#from contextlib import suppress

#with suppress(Exception):
a = time.time()
print(estimateMolMass(MY_LAST_DNA, 'DNA')-(float(len(MY_LAST_DNA)-1)* 18.0153))
print(time.time() - a)