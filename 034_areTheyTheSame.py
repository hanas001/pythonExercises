import math

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# a1 = [11, 14, 19]
# a2 = [11*11, 19*19, 14*14]

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    a2 = []
    for i in array2:
        squareRootI = int(math.sqrt(i))
        a2.append(squareRootI)

    array1 = set(array1)
    a2 = set(a2)
    # print(array1)
    # print(a2)

    if array1 == a2:
        return True
    else:
        return False

print(comp(a1, a2))