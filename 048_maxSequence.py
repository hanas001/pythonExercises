def max_sequence(arr):
    maxsm = 0
    currentsm = 0
    for index in arr:
        currentsm = max(currentsm + index, 0)
        maxsm = max(maxsm, currentsm)

    return maxsm


x = []  #0
# x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  #6
# x = [-2, -1, -3, -4, -1, -2, -1, -5, -4]    # 0
# x = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43] #155

print(max_sequence(x))