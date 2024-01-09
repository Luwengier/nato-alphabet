# numbers = [1, 2, 3]
# Original way:
# new_list = []

# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List Comprehension:
# new_list = [n + 1 for n in numbers]

# doubled_numbers = [n * 2 for n in range(1, 5)]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 4]

# print(short_names)
# print(long_names)

# import random

# student_scores = {student: random.randint(1, 100) for student in names}

scores_dict = {
    "Alex": 14,
    "Beth": 83,
    "Caroline": 56,
    "Dave": 65,
    "Eleanor": 63,
    "Freddie": 38,
}

passed_students = {
    student: score for (student, score) in scores_dict.items() if score >= 60
}

print(passed_students)
