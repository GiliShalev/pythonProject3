# grades = [100, 98, 99, 85, 66, 5]
# print(grades[len(grades) - 1])
# for cell in grades:
#     print("Cell value is: ", cell)
#
# names = ["Gil", "May", "Ori", "Nitay"]
# for cell in names:
#     print(cell)
#
# for i in range(0, len(names) - 1, 1):
#     print(names[i])
#
# print(111 in grades)


# names = ["Gil", "May", "Ori", "Nitay"]
# print(names[0])
# names[0] = 'Moses'
# print(names[0])
# print(names)
#
# print(names[-1])
# print(names[3:4])
# print(names[3])
#
# print(names[1], names[3])
#
# names[0:1] = ["aaa", "bbb", "ccc"]
# print(names)
# names.insert(2, "YYYYYY")
# print(names)
# names.remove("aaa")
# print(names)
# names.append("END")
# print(names)

list_int = [1, 12, 3, 6, 8]
sum1 = 0
for cell_value in list_int:
    if cell_value > 10:
        print(cell_value)
    sum1 += cell_value # sum1 = sum1 + cell_value
print(sum1)
avg = sum1 / len(list_int)
print(avg)

list_cities = ['Aco', 'London', 'Tel Aviv', 'Tokyo']
for city in list_cities:
    if len(city) > 4:
        print(city)
        break

