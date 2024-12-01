# Read the input file and create two lists
with open("input-files/day01-part1.input", "r") as file:
    lines = file.readlines()

list1, list2 = zip(*(line.strip().split() for line in lines))

result_list = [int(value) * list2.count(value) for value in list1]

print("Result List:", sum(result_list))
# 19437052
