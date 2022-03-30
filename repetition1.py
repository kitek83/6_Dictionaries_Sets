#repetition1.py
"""
Repetition without description from previous chapter.
"""
import numpy as np
a = [[77,68,86,73],
     [96,87,89,81],
     [70,90,86,81]]
print(f'len(a)={len(a)}')

for row in a:
    for col in row:
        print(col, end= ' ')
    print()
print()

for i,row in enumerate(a):
    for j, col in enumerate(row):
        print(f'a[{i}][{j}]={a[i][j]}={col}', end = ' ')
    print()
print()

sales = np.arange(6).reshape(2,3)
print(f'sales=\n{sales}')
print(f'len(sales)={len(sales)}')

for row in range(len(sales)):
    for col in range(len(sales[row])):
        print(sales[row][col], end=' ')
    print()
    for col in range(len(sales[row])):
        sales[row][col] = 0

print(f'sales=\n{sales}')
print()

for i,row in enumerate(sales):
    for j,col in enumerate(row):
        sales[i][j] = 33

print(f'sales=\n{sales}')
print()

for i, row in enumerate(sales):
    for j,col in enumerate(row):
        print(f'sales[{i}][{j}]={i}+{j}={i+j}',end=' ')
    print()
print()

total = 0
items = 0

for row in sales:
    for col in row:
        items += 1
        total += col

print(f'average=total:items={total}:{items}={total/items}')

total = 0
items = 0

for row in sales:
    total += sum(row)
    items += len(row)

print(f'average=total/items={total}/{items}={total/items:.3f}')


















