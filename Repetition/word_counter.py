#word_counter.py
"""
Tokenizing a string and counting unique words using for loop.
This repetition.
"""
text = ('this is a sample text with several words '
        'this is more sample text with some different words')
text_dict = {}

#to check:
print(f'text.split():{text.split()}') #creates list of seperated words

for word in text.split():

    if word in text_dict:
        text_dict[word] += 1 #increment value of key in dict
    else:
        text_dict[word] = 1

#to check:
print(f'text_dict: {text_dict}')
print(f'text_dict.items()={text_dict.items()}') #returns list of tuples (word,count)
print()
print(f"{'word':<12}{'count'}")

for word, count in sorted(text_dict.items()): #unpack the list of tuples
    print(f'{word:<12}{count}')

"""
out:
word        count
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
words       2

"""

