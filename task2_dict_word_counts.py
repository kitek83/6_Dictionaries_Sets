#task2_dict_word_counts.py
"""
Tokenizingg a string (braking string into words) and counting unique words.
"""
#module collections containing class Counter
from collections import Counter
#contains counting functionality for the 1st solution of the task2

#1st silution ------------------------

# python automatically concatenates the string's words if we put string in parentheses
text = ('this is a sample text with several words'
        ' this is more sample text with some different words , words , words')
print(text)

#2nd solution - concatenate the text
for i in text:
        print(i,end='')

word_counts = {}

#check text.plit()
print(f'\ntext.split()={text.split()}') #crates a list of separated wpords

#count occurances of each unique word
for word in text.split():   #original text remains unchenged
        if word in word_counts:
                word_counts[word] += 1
        else:
                word_counts[word] = 1
print()
print(f'word_counts={word_counts}')
print()
print(f"{'Word':<12} {'Count'}")

for word, count in sorted(word_counts.items()):   #sorted - sorts in alphabetical order
        print(f'{word:<13}{count}')

print(f'Number of unique words is: {len(word_counts)}.')

print(text)

#2nd solution -----------------------------
print(3*'-------------------------------')

text = ('this is a sample text with several words'
        ' this is more sample text with some different words , words , words')

counter = Counter(text.split())  #creats a dictionary of counted words from text.split()
print(f'counter={counter}')
"""
out: counter=Counter({'words': 4, 'this': 2, 'is': 2, 'sample': 2, 'text': 2, 'with': 2, ',': 2, 'a': 1, 'several': 1, 
'more': 1, 'some': 1, 'different': 1})
"""
for word,count in reversed(counter.items()):  #in reversed order
        print(f'{word:<12}{count}')
print()

#in ascending order using sorted()
for word, count in sorted(counter.items()):
        print(f'{word:<12}{count}')

"""
out:
,           2
different   1
some        1
more        1
words       4
several     1
with        2
text        2
sample      2
a           1
is          2
this        2

,           2
a           1
different   1
is          2
more        1
sample      2
several     1
some        1
text        2
this        2
with        2
words       4

"""


























