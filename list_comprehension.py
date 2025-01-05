# List Comprehension
# new_list = [new_item for n in numbers]
# new_list = [n+1 for n in numbers]

# use python console to see the values line by line
# Python sequences: list, range, string, tuple

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list) # [2, 3, 4]

name = "Peter"
new_list = [l for l in name]
print(new_list) # ['P', 'e', 't', 'e', 'r']

new_list = [r*2 for r in range(1, 5)]
print(new_list) # [2, 4, 6, 8]

# Conditional
# new_list = [new_item for n in list if test]
names = ["Frank", "Emily", "Caroline", "David", "Monica"]
short_names = [name for name in names if len(name) < 6 ]
print(short_names) # ['Frank', 'Emily', 'David']

short_names = [name.upper() for name in names if len(name) > 5 ]
print(short_names) # ['CAROLINE', 'MONICA']

# Convert list of strings to list of ints then filter for even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(l) for l in list_of_strings]
result = [n for n in numbers if n%2 ==0]
print(result)

# Put numbers into new list if both files contains them
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)

