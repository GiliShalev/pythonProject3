hist_grades = {'Dov':95, 'Dana':92, 'Reut':100}
print(hist_grades)
for stud in hist_grades:
    print(stud)

for stud in hist_grades.keys():
    print(stud)

for stud in hist_grades.values():
    print(stud)

for stud, grade in hist_grades.items():
    print(stud, grade)

hist_grades['Dov'] = 97
hist_grades['Rachel'] = 97
print(hist_grades)