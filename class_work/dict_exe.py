moses = {'Geog':77,'History':90,'Math':100}
sum1 = 0
# num_of_grades = 0
for value in moses.values():
    # if str(value).isdigit():
    # num_of_grades += 1
    sum1 += value

moses['Avg'] = sum1 / len(moses)
print(sum1 / len(moses))
print(moses)

car1 = {'Vendor':'Fiat', 'Model':'xxxx'}
car2 = {'Vendor':'Volkswagen', 'Model':'Polo GTI'}

print(car1['Vendor'])
print(car2['Vendor'])

grades = {'Yoel': 70, 'David': 80}
for key, value in grades.items():
    print(key, value)

grades['Yoel'] = 99
print(grades)
print(grades['Yoel'])
grades['Yechezkel'] = 890
print(grades)


