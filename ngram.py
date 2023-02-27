# class for ngram frequencies
from math import log

class NGram:

    def __init__(self, filename):
        self.ngrams = {}
        with open(filename, 'r') as file:
            for line in file.readlines():
                key, count = line.split()
                self.ngrams[key] = int(count)
                self.L = len(key)
        self.N = sum(self.ngrams.values())
        
        for key in self.ngrams.keys():
            self.ngrams[key] = self.ngrams[key] / self.N

    def fitness(self, text):
        f = 0
        for i in range(len(text) - self.L + 1):
            ngram = text[i:i+self.L]
            #print(ngram, end='')
            try:
                #print(log(self.ngrams[ngram]))
                f += log(self.ngrams[ngram])
            except KeyError:
                #print("-15")
                f += -15
        return f / len(text)