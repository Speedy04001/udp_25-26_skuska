# Výpočet četností znaků v textu.
# Daniel Kalakay, 2. ročník, B-SGG
# Zimný semester 2025/6
# Úvod do programování  MZ370P19

class Analyzer:
    support = set(
        "AÁÄBCČDĎEÉFGHIÍJKLĽĹMNŇOÓÔPQRŔSŠTŤUÚVWXYÝZŽ"
        "aáäbcčdďeéfghiíjklľĺmnňoóôpqrŕsštťuúvwxyýzž"
        "0123456789"
        ",.?!;"
    )  # supported character list

    def __init__(self, text):
        self.text = text #store all input text
        self.freq = {}  #dicionary for char counts
        self.total_count = 0   #total number of supported chars

    def analyze(self):
        self.freq.clear()  #dictionary reset
        self.total_count = 0   #total count reset

        for char in self.text:
            if char in Analyzer.support:    #check if char is supported
                self.freq[char] = self.freq.get(char, 0) + 1 #if char is in dictionary add 1, else set to 1
                self.total_count += 1

    def result_print(self):
        sorted_items = sorted(
            self.freq.items(),
            key=lambda x: x[1],
            reverse=True
        ) #sort by abs freq (desc)

        print("Character / Absolute freq. / Relative freq.")

        for char, abs_freq in sorted_items: #for every char and its freq
            rel_freq = abs_freq / self.total_count #relative freq operation
            rel_freq=rel_freq*100
            print(f"{char} / {abs_freq} / {rel_freq:.1f}% textu")

txt = input("Enter text: ") #ui
analyzer = Analyzer(txt)
analyzer.analyze() #start of main script 
analyzer.result_print()  #output printing
