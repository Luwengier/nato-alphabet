# numbers = [1, 2, 3]
# Original way:
# new_list = []

# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List Comprehension:
# new_list = [n + 1 for n in numbers]

# doubled_numbers = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

print(short_names)
