"""
This scripts calculates the repetetiveness through a DNA or 
a Protein sequence
"""

def calcRelativeEntropy(seq, resCodes):
    """
    Calculate a relative entropy (which is the repetetiveness in information tech
    thus an obstacle for variations to have divergency) value for the residues in a 
    sequence compared to a uniform null hypothesis (Null because we expect to have 
    some divergence thus we calculate the repetetiveness if its not null)
    """
    from math import log
    
    N = float(len(seq))
    base = 1.0/len(resCodes)
    
    prop = {}
    for r in resCodes:
        prop[r] = 0
    for r in seq:
        prop[r] += 1
    
