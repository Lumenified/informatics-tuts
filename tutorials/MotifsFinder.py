from Bio import SeqIO

def seq_Loader(seq, formatory, region):
    my_obj = SeqIO.read(seq, formatory)
    my_seq = str(my_obj.seq)
    motif = my_seq.find(region)
    return motif

mySeqObj = SeqIO.read('../Drosophila melanogaster chromosome 3R.fasta', 'fasta')

MY_LAST_DNA = ""
import time
with open("../Drosophila melanogaster chromosome 3R.fasta", "rU") as f:
    my_seq = f.readlines()[1:]
    seq = '\n'.join(my_seq)
    seq = seq.replace("\n", "")
    a = time.time()
    MY_LAST_DNA = seq.replace("N", "")
    print(time.time() - a)

PROFILE =   { 
                'A':[ 61, 16, 352, 3, 354, 268, 360, 222, 155, 56, 83, 82, 82, 68, 77],
                'C':[145, 46, 0, 10, 0, 0, 3, 2, 44, 135, 147, 127, 118, 107, 101],
                'G':[152, 18, 2, 2, 5, 0, 10, 44, 157, 150, 128, 128, 128, 139, 140],
                'T':[ 31, 309, 35, 374, 30, 121, 6, 121, 33, 48, 31, 52, 61, 75, 71]}



def match_dna_profile(_seq, _profile):
    """
    wow
    """
    my_pairs = [[0,None],]
    width = len(_profile['A'])
    for i in range(len(_seq) - width):
        score = 0
        for j in range(width):
            letter = _seq[i+j]
            score += _profile[letter][j]
        """for my_score in best_score:
            if score > my_score:
                
                best_score.append(score)
                best_position.append(i)
        """

        
        if score > my_pairs[-1]:
            my_pairs[i].append(score)
            my_pairs.sort()
        
        if my_pairs.items(). > 4:
            del best_score[0]
            del best_position[0]
        
        
    return best_score, best_position

SCORE, POSITION = match_dna_profile(MY_LAST_DNA, PROFILE)
a = time.time()
#print(score, position, "\n") #MY_LAST_DNA[position:position+15]
for i in range(3):
    print(SCORE[i], POSITION[i], MY_LAST_DNA[POSITION[i]:POSITION[i]+15])
print(time.time()-a)
#a = time.time()
#print(MY_LAST_DNA.find(MY_LAST_DNA[POSITION:POSITION+15]))
#print(time.time() - a)