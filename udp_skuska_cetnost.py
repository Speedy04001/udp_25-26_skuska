# Výpočet četností znaků v textu.
# Daniel Kalakay, 2. ročník, B-SGG
# Zimný semester 2025/6
# Úvod do programování  MZ370P19

class Analyzator:
    def __init__(self, text):
        self.text = text #priradenie vstupu do inštančnej premennej pomocou self
        self.pocetnost = {}  # vytvorenie prazdneho slovnika na pocitanie znakov
        self.support = set(
            "AÁÄBCČDĎEÉFGHIÍJKLĽĹMNŇOÓÔPQRŔSŠTŤUÚVWXYÝZŽ"
            "aáäbcčdďeéfghiíjklľĺmnňoóôpqrŕsštťuúvwxyýzž"
            "0123456789"
            ",.?!;"
        ) # nastavenie mnoziny podporovanych znakov
        self.celk_poc = 0   #priradenie celkovej pocetnosti hodnotu 0

    def hlavnafunkcia(self):
        self.pocetnost.clear()  #vycistenie slovniku
        self.celk_poc = 0   #nastavenie celkovej pocetnosti na 0 pred novym pocitanim

        for znak in self.text:
            if znak in self.support:    #kontrola ci je znak podporovany
                self.pocetnost[znak] = self.pocetnost.get(znak, 0) + 1 #ak znak je v slovniku zvys pocet, inak nastav na 1
                self.celk_poc += 1

    def vypis(self):
        zoradene = sorted(
            self.pocetnost.items(),
            key=lambda x: x[1],
            reverse=True
        ) #zoradenie slovnika podla hodnoty absolutnej pocetnosti, zostupne

        print("Znak / Absolútna / Relatívna")

        for znak, abs_cetnost in zoradene: #pre kazdy znak a jeho pocetnost
            relativna = abs_cetnost / self.celk_poc #vypocet relativnej pocetnosti
            relativna=relativna*100
            print(f"{znak} / {abs_cetnost} / {relativna:.1f}% textu")

txt = input("Zadaj svoj text: ") #ui
analyzator = Analyzator(txt)
analyzator.hlavnafunkcia() #spustenie hlavneho programu
analyzator.vypis()  #výpis výsledku