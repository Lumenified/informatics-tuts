with open("tuts7.txt") as f:
    """
    Dosyadaki degerleri okuyup her stringi birbirinden ayirarak 
    dosyadaki her degeri string olarak aliyoruz ve sonra 
    bunlari integer'a ceviriyoruz.
    """
    #str.split() ve list comprehension kullaniyorum.
    my_file = [int(i) for i in str(f.read()).split()]
    
    #Dosyam artik liste. 
    #Listemin ilk elementi homozigot dominant olanlar
    hz_dominant = my_file[0]
    
    #Ikinci elementi heterozigotlar
    heterozygote = my_file[1]
    
    #Ucuncu elementi ise homozigot resesifler
    hz_recessive = my_file[2]

def MendelFLove(d, h, r, cross_type = "Phenotype"):
    """
    Ilk Yontem: Spagetti! Olsun biz biyologuz :)
    """
    # Populasyon olusturuluyor.
    pop = []
    pop += ["AA" for i in range(d)]# AA Bireyleri ekliyoruz
    pop += ["Aa" for i in range(h)]# Aa Bireyleri ekliyoruz
    pop += ["aa" for i in range(r)]# aa bireyleri ekliyoruz
    # Baslangictaki dominant olacak birey sayim
    my_individuals = 0
    # Caprazlamalar
    cross = []
    j = 0
    # Artik listemdeki bireyleri caprazlamaya baslayabilirim.
    for i in pop:
        # Eslecek bireylerim, listemin 2'nci objesinden basliyor.
        # boylelikle ayni bireyle caprazlamak yerine 
        # bir sonraki bireyi caprazliyorum
        j += 1
        # Ilk bireyim=i, ikinci bireyim ise i'den sonra olan
        # bireylerim yani j'den baslayan "k"
        for k in pop[j:]:
            #i bireyim ve k bireyimi listeme ekliyorum.
            cross.append([i,k])
    # Listem artik hazir. 
    # Caprazlamalarin tamami "cross" listesinde mevcut.
    # Artik karsilastirabilirim.
    for c in cross:
        if c[0]=="AA" and c[1]=="AA":
            #4 bireyimin tamami Homozigot Dominant
            my_individuals +=4
        if c[0]=="AA" and c[1]=="Aa":
            #4 bireyimin tamami Homozigot Dominant
            my_individuals +=4
        if c[0]=="AA" and c[1]=="aa":
            #4 bireyimin tamami Homozigot Dominant
            my_individuals +=4
        if c[0]=="Aa" and c[1]=="Aa":
            #Sadece 3 bireyim Homozigot Dominant
            my_individuals +=3
        if c[0]=="Aa" and c[1]=="aa":
            #Sadece 2 bireyim Homozigot Dominant
            my_individuals +=2
        if c[0]=="aa" and c[1]=="aa":
            #Maalesef Homozigot Dominant birey yok.
            my_individuals +=0
    # DominantBirey/OlusacakPopulasyon
    # Her caprazlama(cross) icin 4 birey
    return round((my_individuals)/(4*len(cross)),10)
#########
print(MendelFLove(hz_dominant,heterozygote,hz_recessive))
#########
def second_edit(t1,t2,t3):
    """
    Oncelikle optimize edebilmek icin formulize etmemiz gerekiyor.
    diyelim ki "k" kadar dominant organizmamiz var ve k-1 kadar 
    dominant organizma ile caprazlayacagiz. Formulumuz 
    "#"  [(k/populasyon)]*[(k-1)/(populasyon-1)]  "#" 
    olurdu. Peki resesiflerden toplam olasilik 1'i cikartirsak 
    nasil olur ?
    O zaman:
    "#"  1 - [( h*r + .25*h*(h-1) + r*(r-1) ) / ( p*(p-1) )]  "#"
    *Not: p, populasyon. h, heterozygote. r, recessive allelerin olasiligi.
    """
    ########################################################################
    p = t1+t2+t3
    ratio = 1 - (( t2*t3 + .25*t2*(t2-1) + t3*(t3-1) ) / ( p*(p-1) ))
    return round(ratio,10)
#########
print(second_edit(hz_dominant,heterozygote,hz_recessive))
#########
