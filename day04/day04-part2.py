lines = []
with open("input-files/day04-part2.input", "r") as file:
    lines = file.read()

content = lines.split("\n")

count = 0
for i in range(1, len(content) - 1):
    for j in range(1, len(content[0]) - 1):
        if content[j][i] == "A":
            cross = (
                content[j - 1][i - 1]
                + content[j - 1][i + 1]
                + content[j + 1][i + 1]
                + content[j + 1][i - 1]
            )
            if cross in ["MMSS", "SMMS", "SSMM", "MSSM"]:
                count += 1

print(count)
# 1880
