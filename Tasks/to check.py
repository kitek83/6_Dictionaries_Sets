# to check.py
"""
Script for checking. It's easy however can be confusing.
"""
import random

frequencies = [0] * 11
tosses = 6000
for toss in range(tosses):
    frequencies[random.randrange(2,13) -2] += 1

print(f'frequencies: {frequencies}')
print(len(frequencies))

values = list(range(2,13))
print(values)
print(len(values))

for i in range(len(frequencies)):
    print(f'frequencies[{i}]={frequencies[i]}')
print()

for val in range(len(values)):
    print(f'values[{val}]={values[val]}')

"""
output:
frequencies: [533, 558, 540, 527, 554, 521, 578, 573, 549, 555, 512]
11
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
11
frequencies[0]=533
frequencies[1]=558
frequencies[2]=540
frequencies[3]=527
frequencies[4]=554
frequencies[5]=521
frequencies[6]=578
frequencies[7]=573
frequencies[8]=549
frequencies[9]=555
frequencies[10]=512

values[0]=2
values[1]=3
values[2]=4
values[3]=5
values[4]=6
values[5]=7
values[6]=8
values[7]=9
values[8]=10
values[9]=11
values[10]=12

"""
