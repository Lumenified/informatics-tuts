with open("tuts7.txt") as f:
    my_file = [int(i) for i in str(f.read()).split()]


def second_edit(pop: dict):
    t2,t3,p = pop[1],pop[2],pop[0]+pop[1]+pop[2]
    return 1 - (( t2*t3 + .25*t2*(t2-1) + t3*(t3-1) ) / ( p*(p-1) ))
    
print(second_edit(my_file))