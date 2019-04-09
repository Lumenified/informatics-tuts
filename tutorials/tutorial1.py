from Bio import SeqIO
"""
for seq_record in SeqIO.parse("ls_orchid.fasta.txt", "fasta"):
    print(seq_record)
    print(repr(seq_record.seq))
    print(len(seq_record))
    pass"""

"""for seq_record in SeqIO.parse("ls_orchid.gbk.txt", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    pass
"""

### to understand how to parse the data in a fasta file
from Bio import SeqIO
"""
records = list(SeqIO.parse("AP006852-1.fasta", "fasta"))
dna = records[0]
print(dna.name)
print(dna.description)
print(dna.seq[:100])
"""
##############################
######Array OBJECTS#########
##############################

import numpy
"""
x = numpy.array([[1,2,3,],[4,5,6,],])
listOfLists = x.tolist()

print(x[1][1])
print(x[1,2])

x = numpy.array([[1,2,3,],[4,5,6,]], dtype=float)

y = numpy.array([[1,2,3,],[4,5,6,]], dtype=numpy.float32)

print(x,y)

print(y.shape) # shape of a numpy array!
print(y.size) #its total size
print(y.ndim) # dimension of an array
x = numpy.zeros((2,3))
print(x)
x = numpy.ones((3,2))
print(x)
x = numpy.identity(3)
print(x)
x = numpy.identity(3, numpy.int)
print(x)

"""
##########TRIGONOMETRIC CALCULATIONS


"""
angles = numpy.array([30.0, 60.0, 90.0, 135.0])
radians = numpy.radians(angles)
cosines = numpy.cos(radians)
print(numpy.log([10.0, 2.71828, 1.0]))
print(numpy.exp([2.302585, 1.0, 0.0]))
print(angles)
print(radians)
print(cosines)
"""

STANDARD_GENETIC_CODE = {
'UUU':'Phe', 'UUC':'Phe',
'UAU':'Tyr', 'UAC':'Tyr',
'UUA':'Leu', 'UCA':'Ser',
'UUG':'Leu', 'UCG':'Ser',
'CUU':'Leu', 'CUC':'Leu',
'CAU':'His', 'CAC':'His',
'CUA':'Leu', 'CUG':'Leu',
'CAA':'Gln', 'CAG':'Gln',
'AUU':'Ile', 'AUC':'Ile',
'AAU':'Asn', 'AAC':'Asn',
'AUA':'Ile', 'ACA':'Thr',
'AUG':'Met', 'ACG':'Thr',
'GUU':'Val', 'GUC':'Val',
'GAU':'Asp', 'GAC':'Asp',
'GUA':'Val', 'GUG':'Val',
'GAA':'Glu', 'GAG':'Glu',
'UCU':'Ser',
'UGU':'Cys',
'UAA':None,
'UAG':None,
'CCU':'Pro',
'CGU':'Arg',
'CCA':'Pro',
'CGA':'Arg',
'ACU':'Thr',
'AGU':'Ser',
'AAA':'Lys',
'AAG':'Lys',
'GCU':'Ala',
'GGU':'Gly',
'GCA':'Ala',
'GGA':'Gly',
'UCC':'Ser',
'UGC':'Cys',
'UGA':None,
'UGG':'Trp',
'CCC':'Pro',
'CGC':'Arg',
'CCG':'Pro',
'CGG':'Arg',
'ACC':'Thr',
'AGC':'Ser',
'AGA':'Arg',
'AGG':'Arg',
'GCC':'Ala',
'GGC':'Gly',
'GCG':'Ala',
'GGG':'Gly'}
#############
dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
###########



"""
print(ProteinTranslation(dnaSeq, STANDARD_GENETIC_CODE))
"""
from time import time
def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te-ts) * 1000)
        else:
            print((method.__name__, (te-ts) * 1000))
        return result
    return timed

from math import sqrt
"""
@timeit
def testFunc(x):
    y = 0
    for i in range(x):
        y += sqrt(i)
    return y

testFunc(10000000)
"""
a = ['G','S','T','P','A']
b = ['A','V','I','L','P']
union = set(a) | set(b)
print(union)
