list_int = [10,20,30,40,50]
list_string = ['aaaa','bbbb','cccc','dddd']
print(list_int[1])
print(list_int[-2])

# Add
list_int[2:2] = [-2,-34,78]
# Replace
list_int[2:5] = [55,66,77]

for i in list_int:
    print(i)

print(list_string[1:3])

list_string.insert (3,"d")
print(list_string)

print(20 in list_int)
print("d" in list_string)

#1, #3, #4
sum1 = 0
for i in list_int:
    if i > 10:
        print(i)
    sum1 += i
print("Sum is:", sum1)
print("Average is:", sum1 / len(list_int))

#2
cities = ["London", "Paris", "Tel Aviv"]
for city in cities:
    if len(city) > 4:
        print(city)
        break