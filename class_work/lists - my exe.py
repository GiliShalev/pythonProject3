# 1
int_list = [11, 12, 3, 89, 17, 42]
for cell in int_list:
    print(cell, ' ', end='')
print()
for cell_index in range(0, len(int_list), 1):
    print(int_list[cell_index], ' ', end='')
# 2
int_list = [-11000, 22, -420000, -1200000, -11000000, -110000]
maxi = int_list[0]
for cell in int_list:
    if cell > maxi:
        maxi = cell
print()
print("Max is:", maxi)

# 3
str_arr = ["David", "went", "to", "the", "store"]
for word in str_arr:
    print(word, end=' ')
print()

# 4
int_list = [888, 1, 45]
int_list[0:0] = [777]
int_list.insert(0, 0)
print(int_list)
int_list[1:2] = [11, 22]
print(int_list)
int_list[0] = int_list[1]
print(int_list)

# 5
letters = ["a", "b", "c"]
for letter in letters:
    print(letter, end='')
print()
for letter_index in range(len(letters) - 1, -1, -1):
    print(letters[letter_index], end='')
print()
# 6
history_grades = {'Moses': 70, 'Yael': 99, 'Yuval': 90}
for name, grade in history_grades.items():
    print(name, grade)

print(history_grades['Moses'])
history_grades['Moses'] = 100
print(history_grades)
history_grades['Nitay'] = 100
print(history_grades)
# print(history_grades["Gili"])
history_grades['Gili'] = 100
print(history_grades["Gili"])
print(history_grades)


# print(int_list)
# print(int_list[2])
# print(len(int_list))
# print(int_list[len(int_list) - 1])