from random import randrange
from typing import Tuple

from ngram import NGram
from autokey import Autokey

class Cracker:
    def __init__(self, k_max=4, verbal=True) -> None:
        self.ng = NGram('english_quadgrams.txt')
        self.k_max = k_max
        self.verbal = verbal
        self.a = Autokey('') # just for letter index

    def crack(self, filename, key_length=0) -> Tuple[str, str]:
        with open(filename, 'r', encoding='UTF-8') as file:
            text = file.read()
            max_fit = -99
            max_fit_key = None
            for period in range(2, 20):
                if key_length != 0 and key_length != period:
                    continue
                
                key = ['A'] * period
                fit = -99
                n = 0 # number of iterations
                while fit < -10:
                    k = key[:]
                    x = randrange(period)

                    for i in range(26):
                        k[x] = self.a.i2a(i)
                        pt = Autokey("".join(k)).decode(text)
                        F = self.ng.fitness(pt)
                        if F > fit:
                            key = k[:]
                            fit = F
                            if self.verbal:
                                print("New key", "".join(key))
                                print("Fitness =", fit)
                    if n > self.k_max * period:
                        break
                    n += 1
                
                # end of guess
                if fit > -10:
                    if self.verbal:
                        print("Key is:", "".join(key))
                        print("Text is:", Autokey("".join(key)).decode(text))
                    return "".join(key), Autokey("".join(key)).decode(text)
                else:
                    if fit > max_fit:
                        max_fit = fit
                        max_fit_key = key
            if max_fit < -10:
                if self.verbal:
                    print("Best guess:")
                    print("Key is:", "".join(max_fit_key))
                    print("Text is:", Autokey("".join(max_fit_key)).decode(text))
                return "".join(key), Autokey("".join(max_fit_key)).decode(text)
                    

                

        

