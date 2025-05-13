# # 1
# for i in range(1, 11, 1):
#     print(i ** 2)
#
# # 2
# fn = "Gil"
# ln = "Shalev"
#
# num_of_letters_fn = 0
# for char in fn:
#     num_of_letters_fn += 1
#
# num_of_letters_ln = 0
# for char in ln:
#     num_of_letters_ln += 1
#
# # 3
# for i in range(1, 100, 1):
#     if i ** 2 == i * 4:
#         print(i)
#         print("Hekef", i * 4)
#         print("Area", i ** 2)
#         break
#
# # 4
# print("Divides by 5 and 3", end='')
# for i in range(1, 100, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         if i < 99:
#             print(i, end=',')
#         else:
#             print(i, end='.')
#
# # 5
# for i in range(1, 100, 1):
#     if '7' in str(i):
#         print("7 is in the number:", i)
#     if i % 7 == 0:
#         print("Divides by 7:",i)

# 6
# city = "London"
# for i in range(0, len(city), 1):
#      print(city[:i + 1])

# 1 Gil
# for i in range(1, 11, 1):
#     for j in range(1, 11, 1):
#         print(i * j, end='')
#     print()

# 2 Gil
for i in range(1, 4, 1):
    for j in range(0, i, 1):
        print('*', end='')
    print()






