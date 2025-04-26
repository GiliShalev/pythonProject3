# list_int = [10,20,30,40,50,12]
# for i in list_int:
#     print(i)
#
# for i in range(0, len(list_int), 1):
#     print(list_int[i])
#
# maxim = 0
# for i in list_int:
#     if i > maxim:
#         maxim = i
#
# print("Max:", maxim)
#
# list_int[2:2] = [-2,-34,78]
# maxim = list_int[0]
# for i in list_int:
#     if i > maxim:
#         maxim = i
#
# print("Max:", maxim)
#
# arr = ["My", "name", "is", "gil"]
# space = ' '
# for word in arr:
#     print(word + space, end='')
# print()
# sentence = ""
# for word in arr:
#     sentence = sentence + word + space
# print(sentence.strip())

list_n = [10,12,3]
list_n[0:0] = [2]
print(list_n)
list_n[1:2] = [222,333]
print(list_n)
list_n[0] = list_n[1]
print(list_n)
list_n.append(21)
list_n.insert(1, 234)
print(list_n)

s = ['a','b','c']
sen = ''
for c in s:
    sen += c
print(sen)
sen = ''
for i in range(len(s), 0, -1):
    sen += s[i - 1]
print(sen)