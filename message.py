import string

class message():
    def __init__(self,text):
        self.text = text.lower()
        self.alphabet = list(string.ascii_lowercase)

    def encode(self, shift):
        newString = ''
        for letter in list(self.text):
            if letter == ' ':
                pass
            else:
                try:
                    newPos = self.alphabet.index(letter) + shift
                except:
                    return 'Fail - Letter not found'
                if newPos > 25:
                    newPos -= 26
                elif newPos < 0:
                    newPos += 26
                letter = self.alphabet[newPos]
            newString += letter
        return newString

    def decode(self, shift):
        return self.encode(shift*-1)

    

