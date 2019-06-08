with open("rosalind_gc.txt", "r") as p:
    my_file = []
    my_id = ""
    my_cache = ""
    my_gen = 0
    for i in p.readlines():
        
        if i[0] == ">":
            if my_gen==0:
                my_id = i[1:]
                my_gen += 1
                continue
            else:
                
                my_file.append([my_id,my_cache])
                my_id = i[1:]
                my_cache = ""
        else:
            my_cache += i[:-1]
        pass
    my_file.append([my_id, my_cache])

def calc_gc_content(seq):
    mylist = []
    for j in range(len(seq)):
        my_ratio = (seq[j][1].count("G") + seq[j][1].count("C"))/len(seq[j][1]) * 100
        mylist.append([seq[j][0], my_ratio])
        pass
    my_return = sorted(mylist, key=lambda x: x[1], reverse=True)
    return str(my_return[0][0]) + str(my_return[0][1])
print(calc_gc_content(my_file))
