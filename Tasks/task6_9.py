# task6_9.py
"""
Using the following dictionary,which maps country names to internet top-level domains
"""
tlds = {'Canada':'ca','United States':'us','Mexico':'mx'}
"""
perform the following tasks and display the results:
"""
#a) check whether dictionary contains key 'Canada':
print(f'"Canada" in tlds: {"Canada" in tlds}')
#to check:
print(f'"Poland" in tlds: {"Poland" in tlds}')
print()

#b) Check whether the dictionary contains the key 'France':
print(f'"France" in tlds: {"France" in tlds}')

#c) Iterate thriugh the key-value pairs and display them into two-column format"
print(f"{'Country':<12}{'domain'}")

for key, val in tlds.items():  #unpack list of tuples
    print(f'{key:<15}{val}')

print()
#d) Add the key-value pair 'Sweden':'sw', which is incorrect
tlds['Sweden'] = 'sw'
tlds.update({'Poland':'pl'})
print(f'tlds: {tlds}')

#e) Update the value for the key 'Sweden' to 'se':
tlds.update({"Sweden":"se"})
print(f'tlds:{tlds}')

#f) Use dictionary comprehension to reverse keys and values:
tlds_reversed = {v:k for k,v in tlds.items()}
print(f'tlds_reversed: {tlds_reversed}')
print()

"""
g) With the result of part f), use a dictionary comprehension to convert
   country names to all uppercase letters.    
"""
tlds_rev_up = {k:v.upper() for k,v in tlds_reversed.items()}
print(f'tlds_rev_up: {tlds_rev_up}')

#to check:
print(f'tlds:{tlds}')  #original tlds{} id unchanged

"""
output:
"Canada" in tlds: True
"Poland" in tlds: False

"France" in tlds: False
Country     domain
Canada         ca
United States  us
Mexico         mx

tlds: {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'sw', 'Poland': 'pl'}
tlds:{'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'se', 'Poland': 'pl'}
tlds_reversed: {'ca': 'Canada', 'us': 'United States', 'mx': 'Mexico', 'se': 'Sweden', 'pl': 'Poland'}

tlds_rev_up: {'ca': 'CANADA', 'us': 'UNITED STATES', 'mx': 'MEXICO', 'se': 'SWEDEN', 'pl': 'POLAND'}
tlds:{'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'se', 'Poland': 'pl'}
"""























