import re

with open("input-files/day03-part1.input", "r") as file:
    content = file.read()

# At the beginning of the program, mul instructions are enabled.
content = "do()" + content

# Regular expressions to match mul(X,Y), do(), and don't()
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Find all matches
mul_matches = list(re.finditer(mul_pattern, content))
do_matches = list(re.finditer(do_pattern, content))
dont_matches = list(re.finditer(dont_pattern, content))

# Initialize sum
sum = 0

# Iterate over mul matches
for mul_match in mul_matches:
    mul_pos = mul_match.start()

    # Check if there is a do() before this mul() and no don't() in between
    valid = False
    for do_match in do_matches:
        if do_match.start() < mul_pos:
            valid = True
            for dont_match in dont_matches:
                if do_match.start() < dont_match.start() < mul_pos:
                    valid = False
                    break
            if valid:
                break

    if valid:
        x, y = int(mul_match.group(1)), int(mul_match.group(2))
        result = x * y
        print(f"mul({x},{y}) = {result}")
        sum += result

print(f"Sum of all valid mul() results: {sum}")
# 111762583
