# Read the input file and create two lists
with open("input-files/day02-part1.input", "r") as file:
    lines = file.readlines()

reports = [line.strip().split() for line in lines]
reports = [[int(num) for num in report] for report in reports]


def is_it_safe(report):
    print(report)
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(0 < abs(report[i] - report[i + 1]) < 4 for i in range(len(report) - 1)):
            return True
    return False


safe = 0
for report in reports:
    print(f"debut {report} safe : {safe}")
    if is_it_safe(report):
        print("safe")
        safe += 1
        continue
    else:
        for i in range(len(report)):
            sub_report = report.copy()
            sub_report.pop(i)
            if is_it_safe(sub_report):
                safe += 1
                print("safe")
                break


print("Safe:", safe)
# 520
