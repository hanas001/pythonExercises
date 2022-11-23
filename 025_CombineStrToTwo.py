""" 'abc' =>  ['ab', 'c_']
'abcdef' => ['ab', 'cd', 'ef']
"""
str = 'asdfads'


def solution(s):
    twoLiteralStr = []
    twoLits = ''
    divider = 0
    lit = ''

    for i in s:
        lit = i

        if divider < 2:
            twoLits += i
            divider += 1

        else:
            divider = 1
            twoLits = ''
            twoLits += i

        if len(twoLits) == 2:
            twoLiteralStr.append(twoLits)

    if len(s) % 2 == 0:
        return twoLiteralStr
    else:
        twoLiteralStr.append(lit + "_")
        return twoLiteralStr


print(solution(str))