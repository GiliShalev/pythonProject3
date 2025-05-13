#1
for i in range(1, 11, 1):
    print(i ** 2)

#2
f_name = "Gil"
l_name = "Shalev"
if len(f_name) > len(l_name):
    print("f_name", f_name)
else:
    print('l_name', l_name)

f_name = "Gili"
f_name_len = 0
for char in f_name:
    print(char)
    f_name_len += 1

l_name_len = 0
for c in l_name:
    l_name_len += 1

if f_name_len > l_name_len:
    print("f_name", f_name_len)
else:
    print('l_name', l_name_len)

#3
for i in range(1, 100, 1):
    if i ** 2 == i * 4:
        print(i)
        break

#4
for i in range(1, 100, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Divides by 3 or 5:", i)

#5
for i in range(1, 100, 1):
    if '7' in str(i):
        print(i, "Contains 7")
    if i % 7 == 0:
        print(i, "No remains")

# 6
city = 'London'
for c in city:
    print(c)

for i in range(0, len(city), 1):
    print(city[0:i + 1])


