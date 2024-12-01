# Read the input file and create two lists
with open("input-files/day01-part1.input", "r") as file:
    lines = file.readlines()

list1, list2 = zip(*(line.strip().split() for line in lines))

list1 = sorted(map(int, list1))
list2 = sorted(map(int, list2))

# Subtract values from list2 to list1
result = [abs(a - b) for a, b in zip(list1, list2)]

print("Result:", sum(result))
# 1882714
