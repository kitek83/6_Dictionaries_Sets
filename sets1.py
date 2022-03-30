#sets1.py
"""
Sets is unordered collection of unique values.
Sets are iterable, they are not sequenced and do not support indexing.
Sets are mutable and eliminates duplicates automatically.
"""
colors = {'red','orange','yellow','green','red','blue'}  #duplicate elimination - 2x red
print(f'colors={colors}')
#out:colors={'yellow', 'red', 'orange', 'green', 'blue'}--> 1x'red'-deleted
print(f'len(colors={len(colors)}') #set is iterable

#operator in/not in with sets
print(f'"red"in colors:{"red" in colors}')
print(f'{"black"not in colors}')
print()

#iterating through sets
for color in colors:
    print(color, end= ' ')

#set with list comprehension
colors_lis = sorted([color.upper() for color in colors])  #creating ordered list (sorted()) from unordered set
print(f'\ncolors_list={colors_lis}')

#eliminates duplicates from the lists
numbers = list(list(range(10)) + list(range(5))) #concatenate 2 list created duplicates
print(f'numbers={numbers}')

#use set to eliminate duplicates
numbers_set = set(numbers)
print(f'numbers={numbers_set}')

#use set to create list without duplicants
list_no_dupl = list(set(numbers))  #list()-hgher ordered function convert set(), which eliminates duplicants
print(f'list_no_dupl={list_no_dupl}')

#check:
print(f'numbers={numbers}')

"""
out for above:
colors={'yellow', 'blue', 'red', 'orange', 'green'}
len(colors=5
"red"in colors:True
True

yellow blue red orange green 
colors_list=['YELLOW', 'BLUE', 'RED', 'ORANGE', 'GREEN']
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
numbers={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
list_no_dupl=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
"""
print(3*'-----------------------------')
"""
task1
Assign the below string to the variable=text, then split into tokens with string's split()
and create set from results. Display a unique word in sorted order.
"""
text = 'to be or not to be that is the question'
text_split = text.split()
print(f'text_split={text_split}')
#out: text_split=['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'a', 'question']

#create set from the results
text_set = set(text_split)  #eliminates 1x 'be' and creates unordered iterable
print(f'text_set: {text_set}')

#diplay words in sorted order
print(sorted(text_set))  #sorted() converts set to list
#out: ['a', 'be', 'is', 'not', 'or', 'question', 'that', 'to']

for word in sorted(set(text.split())):
    print(word, end=' ')
print()
#out: be is not or question that the to

#comparing to sets
print(f'{1,2,3} == {3,2,1}:{ {1,2,3} == {3,2,1}}')


























