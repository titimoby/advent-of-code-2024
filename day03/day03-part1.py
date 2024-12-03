import re

with open("input-files/day03-part1.input", "r") as file:
    content = file.read()

# Regular expression to match mul(X,Y) where X and Y are 1-3 digits
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches
matches = re.findall(pattern, content)

sum = 0
for match in matches:
    x, y = int(match[0]), int(match[1])
    result = x * y
    print(f"mul({x},{y}) = {result}")
    sum += result

print(f"Sum of all mul() results: {sum}")
# 169021493
