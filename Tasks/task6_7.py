# task6_7.py
"""
Write a script that inputs sentence from the user, then uses dictionary
to summuarizes number of occurences of each letter.
Challenge: use a set operation to determine, which letters of original alphabet were not in original string.
"""
from collections import Counter
#counter creates a dictionaty counted letters or words if uses split()

text = ('this is a sample text with several words '
        'this is more sample sample sample text with some different words')

#to check
str1 = {let for let in 'abcd'}
str2 = {let for let in 'defg'}
print(sorted(str1-str2))
print(sorted(str1))

#counting number of occurences each letter in the sentence
counter = Counter(text)

#to check
print(f'counter:{counter}') #counter is a dictionary of counted letters
print()

print(f"{'letter':<12}{'count'}")
text_letters = set()

for letter, count in sorted(counter.items()):  #items() creates list of tuples, which can be sorted()
        print(f'{letter:<12}{count}')
        text_letters |= {letter}   #union augmented assignment for set()

print(f'text_letters: {text_letters}')

"""
Challenge: use a set operation to determine, which letters of original alphabet were not in original string.
"""
alphabet = ' a, ą, b, c, ć, d, e, ę, f, g, h, i, j, k, l, łmnńoópqrsśtuvwxyzźż'
print(alphabet.split())
alphabet_set = set(alphabet) #creates set containing single letters so comma ',' is removed because duplicants are removed
print(alphabet_set)
print()

print('determine, which letters of original alphabet were not in original string:')
determine = alphabet_set - text_letters
print(f'{sorted(list(determine))}')

"""
out:
['a', 'b', 'c']
['a', 'b', 'c', 'd']
counter:Counter({' ': 18, 's': 12, 'e': 12, 't': 9, 'i': 7, 'a': 6, 'm': 6, 'l': 5, 'r': 5, 'h': 4, 'p': 4, 'w': 4, 'o': 4, 'd': 3, 'x': 2, 'f': 2, 'v': 1, 'n': 1})

letter      count
            18
a           6
d           3
e           12
f           2
h           4
i           7
l           5
m           6
n           1
o           4
p           4
r           5
s           12
t           9
v           1
w           4
x           2
text_letters: {'n', ' ', 't', 'p', 's', 'm', 'h', 'r', 'e', 'a', 'd', 'x', 'i', 'l', 'v', 'o', 'f', 'w'}
['a,', 'ą,', 'b,', 'c,', 'ć,', 'd,', 'e,', 'ę,', 'f,', 'g,', 'h,', 'i,', 'j,', 'k,', 'l,', 'łmnńoópqrsśtuvwxyzźż']
{',', 'ł', ' ', 'm', 'e', 'a', 'q', 'x', 'b', 'i', 'o', 'f', 'z', 'ń', 'h', 'r', 'd', 'ś', 'w', 'c', 'ó', 'ź', 't', 's', 'y', 'ć', 'u', 'g', 'v', 'ż', 'n', 'k', 'p', 'j', 'ą', 'l', 'ę'}

determine, which letters of original alphabet were not in original string:
[',', 'b', 'c', 'g', 'j', 'k', 'q', 'u', 'y', 'z', 'ó', 'ą', 'ć', 'ę', 'ł', 'ń', 'ś', 'ź', 'ż']
"""




















