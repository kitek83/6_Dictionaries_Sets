# sets_mat_ops.py
"""
Showing mathematical operations on sets.
"""
#union() or | connect 2 sets
unio_n1 = {1,3,5} | {2,3,4}
print(f'union={unio_n1}')

unio_n2 = {1,3,5}.union({20,20,3,40,40})
print(f'unio_n2={unio_n2}')

#out: unio_n1={1, 2, 3, 4, 5}
#out: unio_n2={1, 3, 20, 5, 40}

#intersection() or '& operator' - set consisting of unique elements that two sets have in common
intersectio_n1 = {1,2,3,4,22} & {5,6,7,3,4,55}
intersectio_n2 = {22,33,44,5,6}.intersection({44,55,54,5,66,6})

print(f'intersectio_n1={intersectio_n1}')
print(f'intersectio_n2={intersectio_n2}')
#out: intersectio_n1={3, 4}

#difference() or operator '-' - set consisting elements of the left operand that are not in he right operand
difference_1 = {1,2,3,4} - {13,4,5,6,7}
difference_2 = {23,4,5,6}.difference({44,5,66,7})
print(f'difference_1={difference_1}')
print(f'difference_2={difference_2}')
print()

#symetric_difference() or '^' - set consisting of the elements of both sets ther are not in common with one another
sym_differ1 = {1,2,3,4} ^ {4,5,6,7}
print(f'sym_differ1={sym_differ1}')

#isdisjoint() - sets are disjoin if they do not have common element
isdisjoint_1 = {1,2,3}.isdisjoint({4,5,6})
print(f'isdisjoint_1={isdisjoint_1}')
print()

"""
Task_2
Given the sets {10,20,30} and {5,10,15,20}, use mathematical set operations
to produce the following sets"
a) {30}
b) {5,15,30}
c) {5,10,15,20,30}
d) {10,20}
"""
set1 = {10,20,30}
set2 = {5,10,15,20}

# a)
print(set1 - set2)
print(f'a): {set1.difference(set2)}')

# b)
print(f'b):{set1 ^ set2}')

# c)
print(f'c): {set1 | set2}')

# d)
print(f'd): {set1 & set2}')
print()
print(3*'-------------------')

"""
Mutable set operations result in new set.
Here we discuss operator and methods that modify an existing set.
"""
#union augmebted asignment |= - performs union set operation, but |= modifies its left operand
numbers = {1,2,3}
numbers |= {4,5,6}
print(f'numbers={numbers}')

#set update() also perform union operation
numbers.update(range(10))
print(f'numbers={numbers}')

#add() - inserts new argument
numbers.add(23)
print(f'numbers={numbers}')

#remove() - removes set argument, but causes KeyError if the arument is not in the set
numbers.remove(0)
print(f'numbers={numbers}')

#discard() - removes argument from the set
numbers.discard(3)
print(f'numbers={numbers}')

#pop() removes set's element, but sets are unordered so you don't know which element will be rerned
numbers_pop = numbers.pop()
print(f'numbers_pop={numbers_pop}')
print(f'numbers={numbers}')

#clear() - empties the set
numbers.clear()
print(f'numbers={numbers}')
#out: numbers=set()

"""
Set comprehensions we create in curly braces like dictionaries.
Let's create a new set containing only even values in the list numbers.
"""
even = {num for num in list(range(1,11)) if num % 2 == 0}
print(f'even={even}')

















