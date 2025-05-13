# sum1 = 0
# while sum1 < 50:
#     num = int(input("Enter a number: "))
#     sum1 = sum1 + num
#
# print(sum1)


num = int(input("Enter a number: "))
num_digits = 0
while num > 0:
    num_digits += 1
    num = int(num / 10)

print(num_digits)



