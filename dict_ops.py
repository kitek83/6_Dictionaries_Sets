#dict_ops.py
"""
Simple operations with dictionaries.
"""
counntry_codes = {'Finlandia':'fi','Poland':'pl','Nepal':'np'}
print(f'country_codes={counntry_codes}')

print(f'len(counntry_codes)={len(counntry_codes)}')

if counntry_codes:
    print('country_codes is not empty')
else:
    print('country_code is empty')

counntry_codes.clear()  #make dictionary empty

if counntry_codes:
    print('country_codes is not empty')
else:
    print('country_code is empty')

days_per_month = {'January':31,'Fbruary':28,'March':31}

print(f'days_per_month.items()={days_per_month.items()}')  #.items() returns tuple
print()
#unpack tuple
for key,val in days_per_month.items():
    print(f'Months:{key} has {val} days.')
print()

#unpack only keys
for key in days_per_month.keys():
    print(f'month:{key}')

#unpack only values
for val in days_per_month.values():
    print(f'day:{val}')

roman_numerals = {'I':1,'II':2,'III':3,'V':10, 'X':100}

#add new numeral
roman_numerals['x'] = 10
roman_numerals['L'] = 50
print(roman_numerals)

#delete key-value pair using del statement
del roman_numerals['X']
print(f'roman_numerals={roman_numerals}')

# roman_numerals={'I': 1, 'II': 2, 'III': 3, 'V': 10, 'x': 10, 'L': 50}
#using method pop() to remove key-value pair, which return poped value
pop_value = roman_numerals.pop('L')  #pop() needs arguement
print(f'pop_value={pop_value}')
print(roman_numerals)

#check pop() with list
list1 = [10,20,30,40]
pop_list = list1.pop() #pop() doesn't  need argument with the list
print(f'pop_list={pop_list}')
print(list1)

#get() wit the dict - returns its arguements corresponding value, doesn't delete this value
value = roman_numerals.get('II')
print(f'value={value}')
print(roman_numerals)
print()

value2 = roman_numerals.get('XXX',"doesn't exist")
print(value2)

#use operator in
print(f"'V' in roman_numerals={'V' in roman_numerals}")
print()

months = days_per_month.keys()
print(f'months={months}')
#out: months=dict_keys(['January', 'Fbruary', 'March'])

for month in months:
    print(f'month: {month}')

#convertin dictionary to the list
print(f'list(days_per_month.keys())={list(days_per_month.keys())}')
print(f'list(days_per_month.values())={list(days_per_month.values())}')
print(f'list(days_per_month.items())={list(days_per_month.items())}')  #returns list of touples (key,value)























