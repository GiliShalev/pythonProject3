age = int(input("Enter age: "))
if age <= 18:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print('Senior')

gender = input("Enter gender(M/F): ")
if gender.lower() == 'm':
    gender = 'Male'
elif gender.lower() == 'f':
    gender = 'Female'
else:
    print("Please enter only m/f")
    exit(-1)
if age <=18:
    age_str = 'Teen'
elif age <= 60:
    age_str = 'Adult'
else:
    age_str = 'Senior'

print(gender + ' ' + age_str)

n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Odd")
else:
    print("Even")

height = int(input("Enter height: "))
if age >= 10 and height >= 150:
    print("OK")
else:
    print("Not OK")

if age < 10 or height < 150:
    print("Not OK")
else:
    print("OK")