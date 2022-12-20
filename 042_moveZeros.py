def move_zeros(lst):
    newList = []
    zeros = []
    for index, number in enumerate(lst):
        # print(index, number)
        if number != 0:
            # lst.pop(index)
            newList.append(number)
        else:
            zeros.append(0)

    # print(newList)
    # print('zeros', zeros)

    for item in zeros:
        newList.append(item)
    # newList.append(zeros)
    return newList

# print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9, 1]))