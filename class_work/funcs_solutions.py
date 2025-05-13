import math

# 1
x = 10
y = 18
diff = x - y
if diff < 0:
    print(math.fabs(diff))
elif diff > 0:
    print(diff * 2)

# 2
s = "the price of the shirt is 25$"
s = s.replace("shirt", "product")
print(s)
if s[0].islower():
    s = s.replace(s[0], s[0].upper(), 1)

if s[0].islower():
    s = s[0].upper() + s[1:]

print(s)





