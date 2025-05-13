# for i in range(10, 0, -1):
#     print(i)

# for i in range(1, 11, 1):
#     if i % 2 == 0:
#         break
#     print(i)
#
# for i in range(1, 11, 1):
#     if i % 2 == 0:
#         continue
#     print(i)

# name = "Gili"
# counter = 0
# for char in name:
#     print(char)
#     counter += 1 # counter = counter + 1
#
# print(counter)

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(i * j, end='')
    print()

t = 987
print(7 in t)