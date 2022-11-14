"""
3
10 10 1 1
3 5 2 4
10 2 5 1
"""

table = []

while True:
    try:
        l = input()
    except EOFError:
        break
    table.append(l)

# print (table)
tries = int(table[0])
# print(tries)

for i in range(1, tries+1):
    # print(i)
    # print(table[i].split())
    line = table[i].split()
    matrixLength1 = int(line[0])
    matrixLength2 = int(line[1])
    coord1 = int(line[2])
    coord2 = int(line[3])
    # print(type(coord1))

    leftLength = coord1 - 1
    rightLength = matrixLength1 - coord1

    if leftLength > rightLength:
        max = leftLength
    else:
        max = rightLength
    # print(max)

    upperLength = coord2 - 1
    lowerLength = matrixLength2 - coord2

    if upperLength > lowerLength:
        high = upperLength
    else:
        high = lowerLength
    # print(high)
    steps = max + high
    print(steps)
