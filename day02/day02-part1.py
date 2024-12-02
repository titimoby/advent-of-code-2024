# Read the input file and create two lists
with open("input-files/day02-part1.input", "r") as file:
    lines = file.readlines()

reports = [line.strip().split() for line in lines]
reports = [[int(num) for num in report] for report in reports]
print(reports)

safe = 0
for report in reports:
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(0 < abs(report[i] - report[i + 1]) < 4 for i in range(len(report) - 1)):
            safe += 1

print("Safe:", safe)
# 472
