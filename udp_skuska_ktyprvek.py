# Nalezení k-tého největšího prvku v posloupnosti.
# Daniel Kalakay, 2. ročník, B-SGG
# Zimný semester 2025/6
# Úvod do programování  MZ370P19

class Analyzator:
    def __init__(self, subor):
        self.subor = subor #ulozenie nazvu vstupneho suboru
        self.sekvencia = [] #vytvorenie prazdnej sekvencie
        self._nacitaj_data() #nacitanie dat

    def _nacitaj_data(self):
        with open(self.subor, "r") as f:
            self.sekvencia = [float(x) for x in f.read().split()] #prevod kazdej hodnoty na typ float

    def nacitaj_najmensi_k(self, k):
        if k < 1 or k > len(self.sekvencia): #kontrola hodnoty k
            raise ValueError("Neplatna hodnota k")

        ind_sekvencia = list(enumerate(self.sekvencia)) # uloženie pôvodných pozícií pomocou enumerate

        ind_sekvencia.sort(key=lambda x: x[1])  # triedenie podľa hodnoty

        pozicia, hodnota = ind_sekvencia[k-1] #vyber k najmeniseho prvku
        return hodnota, pozicia

def main():
    subor = "vstupny_subor_ukol_2.txt"
    funkcia = Analyzator(subor)

    k = int(input("Zadajte k: "))

    hodnota, pozicia = funkcia.nacitaj_najmensi_k(k) #zavolanie funkcie na najdenie k-prvku

    print(f"{k}-ty najmensi prvok ma hodnotu {hodnota}")
    print(f"Povodna pozicia v postupnosti je {pozicia+1}") #+1 pretoze pouzivatel pocita od 1 nie 0

if __name__ == "__main__": #spustenie programu iba ak je subor spusteny priamo
    main()
