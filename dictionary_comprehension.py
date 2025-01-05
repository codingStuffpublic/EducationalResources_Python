import random

names = ["Frank", "Emily", "Caroline", "David", "Monica"]

# students_scores = {new_key:new_value for item in names}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# Conditional Dictionary Comprehension
# new_dic = {new_key:new_value for (key, value) in dictionary if test_condition}
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)