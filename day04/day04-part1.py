def read_input_file(file_path):
    matrix = []
    with open(file_path, "r") as file:
        for line in file:
            matrix.append(line.strip())
    return matrix


file_path = "input-files/day04-part1.input"
matrix = read_input_file(file_path)


def count_patterns(matrix):
    count = 0
    for line in matrix:
        count += line.count("XMAS")
        count += line.count("SAMX")
    return count


count = 0
# count words in origin matrix
count += count_patterns(matrix)
print(count)

# count words in pivoted matrix
pivoted_matrix = ["".join(row[i] for row in matrix) for i in range(len(matrix[0]))]
count += count_patterns(pivoted_matrix)
print(count)


def get_diagonals(matrix):
    diagonals = []

    # Get top-left to bottom-right diagonals
    for i in range(len(matrix)):
        diagonal = []
        row, col = i, 0
        while row >= 0 and col < len(matrix[0]):
            diagonal.append(matrix[row][col])
            row -= 1
            col += 1
        diagonals.append("".join(diagonal))

    for j in range(1, len(matrix[0])):
        diagonal = []
        row, col = len(matrix) - 1, j
        while row >= 0 and col < len(matrix[0]):
            diagonal.append(matrix[row][col])
            row -= 1
            col += 1
        diagonals.append("".join(diagonal))

    # Get top-right to bottom-left diagonals
    for i in range(len(matrix)):
        diagonal = []
        row, col = i, len(matrix[0]) - 1
        while row >= 0 and col >= 0:
            diagonal.append(matrix[row][col])
            row -= 1
            col -= 1
        diagonals.append("".join(diagonal))

    for j in range(len(matrix[0]) - 2, -1, -1):
        diagonal = []
        row, col = len(matrix) - 1, j
        while row >= 0 and col >= 0:
            diagonal.append(matrix[row][col])
            row -= 1
            col -= 1
        diagonals.append("".join(diagonal))

    return diagonals


diagonals = get_diagonals(matrix)
count += count_patterns(diagonals)
print(count)
# 2591
