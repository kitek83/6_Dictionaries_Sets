#dict_comp.py
"""
Using function update() and dictionary comprehensions.
"""
import random
#dict.update({}) - insert key-value to the dict
country_codes = {}
country_codes.update({'Afghasnistan':'AF'})
print(f'country_codes={country_codes}')

country_codes.update({'Albania':'Al'})
print(f'country_codes={country_codes}')

#standard method inserting key-value to the dictionary.
country_codes['Angola'] = 'Ao'
print(f'country_codes={country_codes}')
print()

"""
Task1
Use dictionary compression notation to reverse the key-value of the old dictionary.
"""
months = {'January':1,'February':2,'March':3}
#using dictionary comprehension notation

months2 = {v:k for k,v in months.items()}  #items() returns a tuple, so dictionary comprehension unpack the tuples
print(f'months2={months2}')
#out: months2={1: 'January', 2: 'February', 3: 'March'}

#for check
print(f'months.items()={months.items()}')
#out:months.items()=dict_items([('January', 1), ('February', 2), ('March', 3)])

"""
Task2
Map dictionary list values to average value for each key.
"""
grades = {'Sue':[98,87,94], 'Bob':[84,95,91], 'John':[78,25,33,65]}
grades2 = {k:f'{sum(v)/len(v):.2f}' for k,v in grades.items()} #dict comprehenstion unpacks the tuple

print()
print(f'grades2={grades2}')
#out: grades2={'Sue': '93.00', 'Bob': '90.00', 'John': '50.25'}
print()

"""
Task3
Use a dictionary comprehension notation to crate a dictionary of the numbers 1-5 mapped to their cubes.
"""
cubed_dict = {number:number**3 for number in range(1,6)} #new for me
print(f'cubed_dict={cubed_dict}')

#out: cubed_dict={1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
#for check:
print()
print(f'list(range(100))={list(range(100))}')

dict_calc = {number:f'{number**8/number**23:.32f}' for number in range(1,101)}
print(f'dict_calc={dict_calc}')






















