import matplotlib.pyplot as plt
import numpy as np


def sfad(data):
    minår = 1818
    år_solflekker_observasjoner = {}


    kulvariabel_id = 0
    with open(r"solflekkaktivitet_daglig\solflekkaktivitet_daglig.csv", "r", encoding="utf-8") as file: 
        for n,data in enumerate(file,1):
                dl = data.split(";")
                
                år_solflekker_observasjoner[kulvariabel_id] = dl[0], dl[4], dl[6]
                kulvariabel_id += 1
    
    total_solflekker = 0
    antall_målinger = 0
    maks_daglig = 0
    min_daglig = 999999999
    parse_year = int(år_solflekker_observasjoner[0][0])
    liste_filtrert_etter_år = {}
    print(år_solflekker_observasjoner)
    for entry in år_solflekker_observasjoner:
 
        total_solflekker = 0
        antall_målinger = 0
        maks_daglig = 0
        min_daglig = 999999999
        while int(år_solflekker_observasjoner[entry][0]) == parse_year:
            if int(år_solflekker_observasjoner[entry][1]) != -1:
                total_solflekker += int(år_solflekker_observasjoner[entry][1])
            antall_målinger += int(år_solflekker_observasjoner[entry][2])
            if maks_daglig < int(år_solflekker_observasjoner[entry][1]):
                 maks_daglig = int(år_solflekker_observasjoner[entry][1])
            if (min_daglig > int(år_solflekker_observasjoner[entry][1])) and (int(år_solflekker_observasjoner[entry][1]) != -1):
                min_daglig = int(år_solflekker_observasjoner[entry][1])
            entry+=1
        liste_filtrert_etter_år[parse_year]= total_solflekker, antall_målinger, maks_daglig, min_daglig
        parse_year +=1
        
         
    #print(liste_filtrert_etter_år)




sfad("data")

 #sett alt i år og så sorter de
 #regne dritt i år før man setter de sammen da.
 #år; måned; dag; år-milliår; antall solflekker; standardavvik mellom observasjonene den dagen; antall observasjoner den dagen;
class Maaling_aar:
    def __init__(self):
        self.antall_målinger = -1
        self.total_solflekker= -1
        self.antell_målinger = -1
        self.maks_daglig = -1
        self.min_daglig = -1


#while sfad !=0: 
 #    if 
#if __name__ == "__main__": 