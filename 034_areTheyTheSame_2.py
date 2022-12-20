# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# a1 = [11, 14, 19]
# a2 = [11*11, 19*19, 14*14]

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

c = []
d = []

# c = None
# d = []

# c = True
# d = {}

# c = True
# d = True


def comp(array1, array2):
    a1 = []
    if array1 and array2:
        for i in array1:
            powi = i ** 2
            if powi in array2:
                a1.append(powi)

        array2 = sorted(array2)
        array1 = sorted(a1)

        return array2 == array1

    else:
        return array2 == array1 == []



# print(comp(a1, a2))
# print(comp(a, b))
print(comp(c, d))
