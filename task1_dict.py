#task1_dict.py
"""
Using a dictionary to represent instructor's grade book.
"""
gradebook = {
    'Susan': [92,85,100],
    'Eduardo': [83,95,79],
    'Azizi': [91,89,82],
    'Pantipa': [97,91,92]
}
total_grades = 0
number_grades = 0

print(f'gradebook.items()={gradebook.items()}')
print(list(gradebook.items()))
print()

#calculate and display average of grades od each student using reductions sum() and len():
for name,grades in gradebook.items():
    print(f'Average for {name} is: {sum(grades)}/{len(grades)}={sum(grades)/len(grades):.2f}')
    total_grades += sum(grades)
    number_grades += len(grades)

print()
#print the class average of all student's grades:
print(f"Class's average is: {total_grades}/{number_grades}= {total_grades/number_grades:.2f}")

"""
out:
gradebook.items()=dict_items([('Susan', [92, 85, 100]), ('Eduardo', [83, 95, 79]), ('Azizi', [91, 89, 82]), ('Pantipa', [97, 91, 92])])
[('Susan', [92, 85, 100]), ('Eduardo', [83, 95, 79]), ('Azizi', [91, 89, 82]), ('Pantipa', [97, 91, 92])]

Average for Susan is: 277/3=92.33
Average for Eduardo is: 257/3=85.67
Average for Azizi is: 262/3=87.33
Average for Pantipa is: 280/3=93.33

Class's average is: 1076/12= 89.67
"""
