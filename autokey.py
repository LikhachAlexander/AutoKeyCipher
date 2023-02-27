from string import ascii_uppercase


class Autokey:
    def __init__(self, key, alphabet=ascii_uppercase, pre_filter=str.upper) -> None:
        self.alphabet = alphabet
        self.pre_filter = pre_filter
        self.key = self.filter(key)

    @staticmethod
    def load_alphabet(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            result = [] 
            [result.append(x) for x in file.read() if x not in result] 
            return "".join(result)

    def i2a(self, i: int):
        i = i % len(self.alphabet)
        return self.alphabet[i]

    def a2i(self, a: str):
        if a in self.alphabet:
            return self.alphabet.index(a)
        else:
            return -1

    def filter(self, text):
        if self.pre_filter is not None:
            text = self.pre_filter(text)
        return ''.join([c for c in text if c in self.alphabet])

    def encode(self, s: str) -> str:
        s = self.filter(s)
        encoded_text = ""
        for (i, c) in enumerate(s):
            if i < len(self.key):
                key_c = self.key[i]
            else:
                key_c = s[i - len(self.key)]
            encoded_text += self.i2a(self.a2i(c) + self.a2i(key_c))
        return encoded_text

    def decode(self, s: str) -> str:
        s = self.filter(s)
        decoded_text = ""
        for (i, c) in enumerate(s):
            if i < len(self.key):
                key_c = self.key[i]
            else:
                key_c = decoded_text[i - len(self.key)]
            decoded_text += self.i2a(self.a2i(c) - self.a2i(key_c))
        return decoded_text
