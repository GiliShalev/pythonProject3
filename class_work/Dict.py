grades = {'Moses':99,'Yael':100,'Yariv':87}
print(grades)
print(grades['Yael'])
grades['Moses'] = 93
print(grades)
grades['Haym'] = 80
print(grades)
grades["fff"] = 0
print(grades["fff"])
print(grades)

for key, value in grades.items():
    print(key, value)

for key in grades.keys():
    print(key)

for value in grades.values():
    print(value)


