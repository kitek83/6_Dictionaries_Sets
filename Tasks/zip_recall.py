# zip_recall.py
"""
Recall how zip() works.
"""
names = ['Amanda','Kris','Jack','Bob']
grades = [1,2,3,4]

for name, grade in zip(names, grades):
    print(f'name:{name:<8}-->grade: {grade}')

#to check:
print(f'{list(zip(names,grades))}')