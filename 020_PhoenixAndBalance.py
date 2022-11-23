"""
2
2
4

1
4

5
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
30

"""

table = []

while True:
    try:
        l = input()
    except EOFError:
        break
    table.append(l)

testCases = int(table[0])
table.pop(0)

def powFunction(number):
    calcTable = []
    while number >= 1:
        result = 2**number
        calcTable.append(result)
        number -= 1
    return calcTable

def max(someList):
    max = 0
    for f in range(len(someList)):
        currentNumber = int(someList[f])
        if currentNumber > max:
            max = currentNumber
    return max

def min(someList):
    min = someList[0]
    for f in range(len(someList)):
        # print("f", f)

        currentNumber = int(someList[f])
        # print("cN",currentNumber)
        # print(type(currentNumber))

        if currentNumber < min:
            min = currentNumber
    return min

while testCases > 0:
    b = 0
    a = 0
    lenA = 0
    lenB = 0
    faceValue = powFunction(int(table[0]))
    # print("table", table)
    # print("table zero", table[0])
    # print("faceValue", faceValue)
    while len(faceValue) > 0:
        if a < b and lenA <= lenB:
            maximum = max(faceValue)
            a += maximum
            faceValue.remove(maximum)
            lenA += 1
        elif a <= b and lenA <= lenB:
            maximum = max(faceValue)
            b += maximum
            faceValue.remove(maximum)
            lenB += 1
        else:
            minimum = min(faceValue)
            b += minimum
            faceValue.remove(minimum)
            lenB += 1

    difference = abs(a - b)

    print(difference)
    testCases -= 1
    table.pop(0)