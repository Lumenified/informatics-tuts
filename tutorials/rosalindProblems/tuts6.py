with open("rosalind_hamm.txt") as p:
    f_seq = ""
    my_whole_seq = ""
    my_whole_seq += str(p.read()).replace("\n", "")

def Hamming_Calculation(seq):
    counter = 0
    for i in range(int(len(seq)/2)):
        if seq[i]!=seq[(int(len(seq)/2))+i]:
            counter += 1
    return counter

print(Hamming_Calculation(my_whole_seq))