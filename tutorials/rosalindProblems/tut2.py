def transcribe(s):
    mylist = ""
    for i in s:
        if i=="T":
            i="U"
        mylist = mylist + i
    print(mylist)
my_seq = "AGCGAGGTCGTCAACCGGAGTCTTGGACGGTACCTCACACAATTTCAGCTCGCCTCGCCGCGAAGTCAGAGTAAAGTAGACAGATTATATTAAAAAGGGTCTAGGAGTAGTCTTCGACACAAATAACCCTAAGAGCTGTCTTGCCTAAGCATGAGCACTTCCGTTCGGCTATGCATTGAAAGAGATCGCTAGTACCGCCGACTATCTGCAATATTTAATGCGAAAGAGACTATGATGCACGTATACGGTAAGAGGTCGTAAAATGCTGCCGGTGCGGTCCCGCATGTATTCATCGATACTGCCTCCTAATCATGATGGTAGGTCCCCTCCATCCGACAACCGATCGTCCCCTAGACATCGTACATGCCAGTTCAGGTCAAAATAGATCGAAGCAGGGACGGCGAGGGCCCGATTCAACAGAATAACATAATGTACTGACCCTGATATAATTCCTCTCACGCTATACCCAAAGCGTCCGAACAAGGTAACGGACAATAGCCATCCCGTAGTCGAGCGCGGGACACCCTGAGCTCATCGCTTACCCCTCGGGTGTCTACCTCGGTGGCTCGATTTCCTATCACCAAATCGTTTCTAGTTAGCCCAACCAAACCCCAGGTTAAGAGATCCACACGCGTGCTGCCACTTCACCGCGTATACAAGACGCACCCGGGTAACTAGGTAATGAAATTTGTCTTGTTGTTGGATTCCCCATTACAACTCCGCCGGGTAATTTTATCTTCGTTGGGCGGCGGGCACTGCTGTCAGATAACTCCGGGCAATCTCCGTACGTGGTCGTCTCTACGCAAGCTGAAGTGGGAAAACCCGCCCGACAACTGGGTGGATCTAGTGCTTGTCGGGCGTCACCGAGTTGTGTCGAGATCGCTACCTGGGTACGTTGTCCGCTGTCAAAAGAGGAAGAAAATCATTGCACGAATGATAGTCCCAACTAGGAACGGCCGGGAACAGGGGACTACGCCAAG"

transcribe(my_seq)