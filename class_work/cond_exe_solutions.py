gender = input("Please enter your gender (M/F): ").upper()
age = int(input("Please enter your age: "))

if age <= 18:
    age_str = "Teenager"
elif age <= 60:
    age_str = "Adult"
else:
    age_str = "Master"

if gender == "M":
    gender = "Male"
elif gender == "F":
    gender = "Female"
else:
    print("Only M/F are valid options")
    exit(-1)

print(gender, age_str)


h = 160
age = 18
if age >= 10 and h >= 150:
    print("Yes")
else:
    print("No")

if age < 10 or h < 150:
    print("No")
else:
    print("Yes")

a = 9
b = 8
c = 5

