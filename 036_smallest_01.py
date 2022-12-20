def smallest(n):
    strN = str(n)
    minNumber = min(strN)
    minIndex = strN.index(minNumber)
    result = []

    # print('minimum', minNumber, 'minimum index', minIndex)

    for i in range(len(strN)):
        index = i
        item = int(strN[i])
        # print('index', index, 'item', item)

        if item == int(minNumber):
            print(item, minNumber)
            # print(strN)
            strN = strN.replace(minNumber, '', 1)
            # print(strN)
            strN = minNumber + strN
            # print(strN)


            # print(type(strN), type(minNumber), type(minIndex))

            result = [strN] + [str(minIndex)] + [0]
            # print('result', result)
            break

    return result


print(smallest(261235))     #[126235, 2, 0]
# print(smallest(209917))     #[29917, 0, 1]
print(smallest(285365))     #[238565, 3, 1]
# print(smallest(269045))     #[26945, 3, 0]
# print(smallest(296837))     #[239687, 4, 1]