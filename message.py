import string
import math

class message():
    def __init__(self,text):
        self.text = text.lower()
        self.alphabet = list(string.ascii_lowercase)
        self.vigenereSquare = []

    def caesar(self, shift):
        newString = ''
        for letter in list(self.text):
            if letter == ' ':
                pass
            else:
                try:
                    newPos = self.alphabet.index(letter) + shift
                except:
                    return 'Fail - Letter not found'
                if (newPos > 25) or (newPos < 0):
                    m = math.ceil(newPos/26) - 1
                    newPos -= m*26
                letter = self.alphabet[newPos]
            newString += letter
        return newString

    def createVSquare(self):
        self.vigenereSquare.append(self.alphabet.copy())
        alpha = self.alphabet
        for i in range(len(alpha)-2):
            alpha.append(alpha[0])
            alpha = alpha[1:]
            self.vigenereSquare.append(alpha.copy())

    def vigenere(self, key):
        newString = ''
        self.createVSquare()
        m = math.ceil(len(self.text)/len(key))
        j = len(key)
        key = m*key
        key = key[:-1*(m*j - len(self.text))]
        for i in range(len(self.text)):
            letter = self.vigenereSquare[self.alphabet.index(key[i])][self.alphabet.index(self.text[i])]
            newString += letter
        return newString
    

