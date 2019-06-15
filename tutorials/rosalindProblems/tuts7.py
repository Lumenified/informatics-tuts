from scipy.special import comb
with open("tuts7.txt") as f:
    my_file = str(f.read()).split()
def MendelFLove(my_array: dict, cross_type = "Phenotype"):
    pop = []
    pop += ["AA" for i in range(int(my_array[0]))]
    pop += ["Aa" for i in range(int(my_array[1]))]
    pop += ["aa" for i in range(int(my_array[2]))]
    my_ratio = 0
    cross = []
    j = 0
    for i in pop:
        j += 1
        for k in pop[j:]:
            cross.append([i,k])
    for d in cross:
        if d[0]=="AA" and d[1]=="AA":
            my_ratio +=4
        if d[0]=="AA" and d[1]=="Aa":
            my_ratio +=4
        if d[0]=="AA" and d[1]=="aa":
            my_ratio +=4
        if d[0]=="Aa" and d[1]=="Aa":
            my_ratio +=3
        if d[0]=="Aa" and d[1]=="aa":
            my_ratio +=2
        if d[0]=="aa" and d[1]=="aa":
            my_ratio +=0
    return (my_ratio/4/comb(int(my_array[0])+int(my_array[1])+int(my_array[2]),2))
print(MendelFLove(my_file))