keys = ["c", "d", "e", "f", "g", "a", "b", "c"]

piano_tuples = ("do", "re", "mi", "fa")

# 2, 3, 4
print(keys[2:5]) # ['e', 'f', 'g']

# from 4
print(keys[4:]) # ['g', 'a', 'b', 'c']

# til 2
print(keys[:2]) # ['c', 'd']

# third param = increment
print(keys[2:5:2]) # ['e', 'g']

# every second element
print(keys[::2]) # ['c', 'e', 'g', 'b']

# reverse the list
print(keys[::-1]) # ['c', 'b', 'a', 'g', 'f', 'e', 'd', 'c']

print(piano_tuples[2:4]) # ('mi', 'fa')

