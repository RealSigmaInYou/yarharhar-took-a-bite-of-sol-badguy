import matplotlib.pyplot as plt
import numpy as np

class Maaling_aar:
    def __init__(self):
        år_solflekker_observasjoner = {} #lager dictionary


        kulvariabel_id = 0
        with open(r"yarharhar-took-a-bite-of-sol-badguy-main\solflekkaktivitet_daglig.csv", "r", encoding="utf-8") as file: 
            for n,data in enumerate(file,1):
                    dl = data.split(";")
                    
                    år_solflekker_observasjoner[kulvariabel_id] = dl[0], dl[4], dl[6] #implementerer data til dictionarien
                    kulvariabel_id += 1
        
        total_solflekker = 0#gjør klar variabler for bruk
        antall_målinger = 0
        maks_daglig = 0
        min_daglig = str
        parse_year = int(år_solflekker_observasjoner[0][0]) #parse_year sitt utgangspunkt er den første verdien i den første inndelingen i år_solflekker_observasjoner. den blir altså 1818 som en string. derfor gjør vi den om til en integer for at vi skal kunne jobbe med den som en integer. (man kan kun gjøre mattematiske funksjoner med integers, floats, og andre nummer-datatyper)
        self.liste_filtrert_etter_år = {}
        for entry in år_solflekker_observasjoner: #går gjennom hver entry i listen og filtrerer dataen etter: år, total mengde solflekker, total mengde målinger det året, maks antall solflekker det året,og minste antall solflekker det året

            if int(år_solflekker_observasjoner[entry][1]) != -1:
                total_solflekker += int(år_solflekker_observasjoner[entry][1])
            else:
                total_solflekker += 0
            antall_målinger += int(år_solflekker_observasjoner[entry][2])
            if maks_daglig < int(år_solflekker_observasjoner[entry][1]):
                maks_daglig = int(år_solflekker_observasjoner[entry][1])
            if  min_daglig == str or ((int(min_daglig) > int(år_solflekker_observasjoner[entry][1])) and (int(år_solflekker_observasjoner[entry][1]) != -1)):
                min_daglig = int(år_solflekker_observasjoner[entry][1])
            
            self.liste_filtrert_etter_år[parse_year]= total_solflekker, antall_målinger, maks_daglig, min_daglig 
            if parse_year <= int(år_solflekker_observasjoner[entry][0]): #dersom parseyear er mindre eller lik året for-loopen er på, så resetter den variablene, og legger til 1 til parseyear. parseyear blir brukt til å 
                parse_year +=1
                total_solflekker = 0
                antall_målinger = 0
                maks_daglig = 0
                min_daglig = str
        print(self.liste_filtrert_etter_år)
        self.maalinger()

    def maalinger(self):
        total_solflekker_år = [] #gjør klar arrays
        antall_målinger_år = []
        maks_daglig_år = []
        min_daglig_år = []
        alle_år = [y for y in self.liste_filtrert_etter_år]
        for år in self.liste_filtrert_etter_år: #filtrerer data i hver sin array. her appender vi dataen slik at vi kan lett hente dataen som vi trenger
            total_solflekker_år.append(self.liste_filtrert_etter_år[år][0])
            antall_målinger_år.append(self.liste_filtrert_etter_år[år][1])
            maks_daglig_år.append(self.liste_filtrert_etter_år[år][2])
            min_daglig_år.append(self.liste_filtrert_etter_år[år][3])
        fig = plt.figure() #lager figur for plotte på data
        fig, ax = plt.subplots() 
        ax.plot(alle_år, maks_daglig_år, label="meste mengde solflekker/år")
        ax.plot(alle_år, min_daglig_år, label="minste mengde solflekker/år") #legger til dataen til i figuren. første verdien er x-aksen, og den andre er y-aksen
        ax.plot(alle_år, total_solflekker_år, label="Total solflekker/år")
        plt.show()

#problemer: 
#   - Den lager to figurer.
#   - Jeg vet ikke om den følger oppgavebeskrivelsen, men det får du finne ut av. dette er mer eller mindre en oversikt over hvordan man kan gjøre det 

if __name__ == "__main__":
    Maaling_aar()
