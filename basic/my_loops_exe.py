sum1 = 0
while sum1 < 50:
    num = int(input("Enter a number: "))
    sum1 += num

print(sum1)

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(i * j, end='')
    print()

for i in range(1, 4, 1):
    for j in range(1, i + 1, 1):
        print('*', end='')
    print()

num_digits = 1
num = int(input("Enter a number: "))
while int(num / 10) > 0:
    num_digits += 1
    num /= 10
print(num_digits)
