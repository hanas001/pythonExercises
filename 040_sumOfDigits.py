def digital_root(n):
    strN = str(n)

    while len(strN) > 1:
        sum = 0
        # print(strN, type(strN))
        for i in strN:
            sum += int(i)

        # print(sum)
        strN = str(sum)


    return int(strN)


# print(digital_root(16))
# print(digital_root(942))
# print(digital_root(132189))
print(digital_root(493193))