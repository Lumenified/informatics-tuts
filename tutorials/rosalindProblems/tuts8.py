from Bio.Seq import translate
with open("rosalind_prot.txt") as p:
    myfile = p.read()
print(translate(myfile,stop_symbol=""))