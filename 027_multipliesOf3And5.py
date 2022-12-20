number = 200

def solution(number):
    tempSum3 = 0
    tempSum5 = 0
    totalSum = []
    result = 0
    for i in range(number):
        tempSum3 = 3 * i
        if tempSum3 < number:
            totalSum.append(tempSum3)

    for k in range(number):
        tempSum5 = 5 * k
        if tempSum5 < number:
            totalSum.append(tempSum5)

    totalSum = set(totalSum)
    # print(totalSum)

    for j in totalSum:
        result += int(j)

    # print(result)

    return result

print(solution(number))