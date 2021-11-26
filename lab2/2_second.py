import re
import string


class Text:
    def __init__(self, name):
        try:
            self.file = name
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def chartes(self):
        file = open(self.file)
        num = 0
        for line in file:
            for char in line:
                if char not in string.whitespace:
                    num += 1
        file.close()
        return num

    def number_words(self):
        file = open(self.file)
        num = 0
        for line in file:
            num += len(re.findall(r"\w+", line))
        file.close()
        return num

    def number_of_offers(self):
        file = open(self.file)
        num = 0
        for line in file:
            num += len(re.findall(r"\w+[.?!]+", line))
        file.close()
        return num


text = Text('My_text.txt')
print(f"Characters: {text.chartes()}")
print(f"Number of words: {text.number_words()}")
print(f"Number of offers: {text.number_of_offers()}")
