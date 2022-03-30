#task6_5.py
"""
Write script that uses a dictionary to determine and print the duplicated words and number of duplicate
words in sentence.
"""
from collections import Counter
#Counter count occurances of the letters or words in the sentence and return a dictionary

sentence = ('this is a sample text with several words '
        'this is more sample sample sample text with some different words')

counter = Counter(sentence.split()) #split() returns a list of seperated words

#to check:
print(f'counter:{counter}') #return a dictionary of counted words
print(f'counter.items():{counter.items()}') #returns list of tuples to be unpacked
print()

#print duplicated words - words with counts > 1
print(f"{'duplicated_word':<22}{'count'}")   #:< - format specifier counts number of letters of the word and add free space if satys any

num = 0
for word, count in sorted(counter.items()): #unpack the list of tuples in alphabetic order

        if count > 1:#returns only diplicated words
                num += 1  #counts the number duplicated words
                print(f'{num}.{word.upper():<22}{count}') #all lettrs must be upper() or lower() to get alphabetical order

#counting the number of duplicated words
print(f'number of dublicated words = {num}')
























