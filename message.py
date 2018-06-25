import string
import math

class message():
    def __init__(self,text):
        self.text = text.lower()
        self.alphabet = list(string.ascii_lowercase)

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


    

