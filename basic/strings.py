# num =1
# num_as_string = str(1)
# string_num_only = '123'
# all_nums = string_num_only.isdigit()
# mixed = '123qw'
# mixed_is_nums = mixed.isdigit()
# string_as_num = int(string_num_only)
# result = string_as_num -1
# print (result)
#
# s = "abcd"
# print(len(s))
# i = s.index('d')
# print(i)
# s1 = "a b c g    "
# print(s1.strip())
# print('a' in s)
# print('k' in s)
#
# #1
# first_name = 'Gil'
# last_name = 'Shalev'
# print(len(first_name))
# print(len(first_name))
#
# #2
# print(first_name)
# print(last_name)

full_name = "Gil Shalev"
ind = full_name.index(' ')
fn = full_name[:ind]
ln = full_name[ind + 1:]
print(fn[0:1])
print(ln[0:1])
# Same as
print(fn[0])
print(ln[0])

arr = full_name.split(' ')
print(arr[0])
print(arr[1])
print(arr[0][:1])

print(fn == ln)

full_name = "Gil Shalev"
full_name_for_print_in_2_line = full_name.replace(" ", "\n")
print(full_name_for_print_in_2_line)


full_name = "Gil Shalev"
arr_name = full_name.split(' ')
print(arr_name[0][0])
print(arr_name[1][0])

s = "Gil Shalev"
print(s[4])


