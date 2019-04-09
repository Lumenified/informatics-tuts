def ProteinTranslation(_seq, _geneticCode):
    
    """This function translates a nucleic acid sequence into a
        protein sequence, until the end or until it comes across 
        a stop codon. Firstly we define the alphabet to make a matchup in it
        then we put the sequence that we have. Then we convert the sequence to 
        the aminoacids by comparing the codons!
    """
    seq = _seq.replace('T', 'U') #Make sure that we have an RNA sequence
    proteinSeq = []

    i = 0

    while i+2 < len(seq):
        codon = seq[i:i+3]
        aminoAcid = _geneticCode[codon]
        if aminoAcid is None:
            break
        
        proteinSeq.append(aminoAcid)
        i += 3
    return proteinSeq


    pass