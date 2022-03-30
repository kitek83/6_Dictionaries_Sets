# task6_6.py
"""
Duplicate word removal with the usage of set().
Write the function that receives list of words, then displays in alphabetical order only unigue words.
The function should use set() to get unique word from the list.
"""
text = ('this is a sample text with several words '
        'this is more sample sample sample text with some different words')

list_text = text.split() #split() creates list of seperated words
#check:
print(f'list_text:{list_text}')
print(f'list_text_sorted:{sorted(list_text)}')  #sorted also creates the list

def unique(text):
    # display only unique words in alphabetical order:

    for word in sorted(set(word.upper() for word in text.split())): #sorted creates sorted list from unorded set. Set() removes duplicates.
        print(word, end=' ')

    print()
print()

print('Unique words in alphabetical order from function unicue():')
unique(text) #call func

text2 = 'Prevent common common pitfalls pitfalls : avoid SQL injection attacks , store database credentials securely , ' \
        'and Optimize the Performance of your Applications'
unique(text2) #call func