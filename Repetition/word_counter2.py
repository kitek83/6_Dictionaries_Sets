#word_counter2.py
"""
Tokenizing a string and counting unique words using module collection's Counter class.
This repetition.
"""
from collections import Counter

text = ('this is a sample text with several words '
        'this is more sample text with some different words')
counter2 = Counter(text) #creating object, creates dictionary {letter of string:value of occurence}
counter = Counter(text.split()) #returns dictionary of counted words, text.split() - creates list of seperated words

#to check:
print(f'counter2:{counter2}') #counts occurance of each letter from the text
print(f'counter:{counter}')
print()

print(f"{'word':<12}{'count'}")

for word, count in sorted(counter.items()):
        print(f'{word:<12}{count}')

