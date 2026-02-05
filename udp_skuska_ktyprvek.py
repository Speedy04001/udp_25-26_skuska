# Nalezení k-tého největšího prvku v posloupnosti.
# Daniel Kalakay, 2. ročník, B-SGG
# Zimný semester 2025/6
# Úvod do programování  MZ370P19

class Analyzer:
    def __init__(self):
        self.sequence = [] #store input sequence

    def load_data(self, filename):
        with open(filename, "r") as f:
            self.sequence = [float(x) for x in f.read().split()]  #convert input values to float

    def _sel_sort(self, data): #selection sort sorting function [handwritten :)]
        n = len(data) #store length of the seq
        for i in range(n - 1): #iterate over each element except last
            min_index = i #assume pos i holds the min.
            for j in range(i + 1, n): #check all elements in unsorted part
                if data[j][1] < data[min_index][1]: #compare val.
                    min_index = j #update index if smaller el. found
            data[i], data[min_index] = data[min_index], data[i] #swap current with new minimum

    def find_k_small(self, k):
        if k < 1 or k > len(self.sequence): #validate if K is within bounds
            raise ValueError("Invalid value of k") #error message i K is not valid
        indexed_sequence = list(enumerate(self.sequence)) #store original positions
        self._sel_sort(indexed_sequence)   #sort using sorting algorithm _sel_sort
        position, value = indexed_sequence[k - 1] #select k smallest element
        return value, position

def main():
    filename = "vstupny_subor_ukol_2.txt" #input file//can be changed to input("filename.txt :") for user custom file
    analyzer = Analyzer()
    analyzer.load_data(filename)

    k = int(input("Enter k: ")) #user input for K

    value, position = analyzer.find_k_small(k)

    print(f"The {k}-th smallest element has value {value}")
    print(f"Original position in the sequence is {position + 1}") #+1 because user indexing starts from 1

if __name__ == "__main__":
    main() #execute main func. if script is run direct.
