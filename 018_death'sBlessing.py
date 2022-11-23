"""
4
1
10
0
3
100 1 100
1 100 1
4
2 6 7 3
3 6 0 5
2
1000000000 1000000000
1000000000 1000000000
"""

table = []

while True:
    try:
        line = input()
    except EOFError:
        break
    table.append(line)

# print(table)
testCases = int(table[0])
tableLength = len(table)-1
print(tableLength)

dictTable = {}
unitHealth = []

for unit in range(1, tableLength, 3):
    dictTable[table[unit]] = 0
    # print("J", unit)
    # print(table[unit])

for j in range(2, tableLength, 3):
    unitHealth += table[j].split()

print(dictTable)
print(unitHealth)
# for case in range(1, testCases+1):

    # print(case)
    # print(type(case))
    # print(table[case])