#task3_count.py
"""
Use a comprehension to create a list o 50 random integers in the range 1-5.
Summarize list with Counter from collections standard library.
Display the results in two column format.
"""
import random
from collections import Counter

#use comprehension
list_50 = [random.randrange(1,6) for x in range(50)]
print(f'list_50={list_50}')
print(len(list_50))

#summarize list with Counter
counter = Counter(list_50)  #creates dictionary, which shows how naby times randrage(1,6) appear in the list of 50 values
print(f'counter={counter}')
"""
out: counter=Counter({1: 15, 5: 10, 4: 9, 2: 9, 3: 7})
"""
print()

print(f'sorted(counter.items())={sorted(counter.items())}')  #sort accoring the 1st value=key, items() return list of tuples

for val,count in sorted(counter.items()): #unpack the tuple
    print(f'{val:<12}{count}')

"""
out:
counter=Counter({2: 16, 4: 11, 1: 8, 5: 8, 3: 7})

sorted(counter.items())=[(1, 8), (2, 16), (3, 7), (4, 11), (5, 8)]
1           8
2           16
3           7
4           11
5           8

"""























