import re

with open("input-files/day03-part1.input", "r") as file:
    content = file.read()

# At the beginning of the program, mul instructions are enabled.
content = "do()" + content

# Regular expressions to match mul(X,Y), do(), and don't()
mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

# Find all matches
mul_matches = mul_pattern.finditer(content)
do_positions = [match.start() for match in do_pattern.finditer(content)]
dont_positions = [match.start() for match in dont_pattern.finditer(content)]

# Initialize sum
sum = 0

# Iterate over mul matches
for mul_match in mul_matches:
    mul_pos = mul_match.start()
    valid = any(
        do_pos < mul_pos
        and not any(do_pos < dont_pos < mul_pos for dont_pos in dont_positions)
        for do_pos in do_positions
    )

    if valid:
        x, y = map(int, mul_match.groups())
        result = x * y
        print(f"mul({x},{y}) = {result}")
        sum += result

print(f"Sum of all valid mul() results: {sum}")
# 111762583
