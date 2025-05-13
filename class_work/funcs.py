from math import fabs

def ret_2_values():
    return 1, 2, 3

def my_func(num):
    if num > 5:
        return True
    print("Hello")
    return False

y, u, i = ret_2_values()
print(y)

x = my_func(99)
print(x)

x = my_func(2)
print(x)

print(fabs(-1))