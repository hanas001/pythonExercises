def valid_parentheses(string):
    openParent = 0
    closeParent = 0

    if string == "":
        return True

    elif string[0] == ')' or string[-1] == '(':
        return False

    else:
        for i in string:
            if i == '(':
                openParent += 1
            elif i == ')':
                closeParent += 1

        if openParent == closeParent:
            return True
        else:
            return False

# print(valid_parentheses("()"))                   #True
# print(valid_parentheses(")(()))"))               #False
# print(valid_parentheses("("))                    #False
# print(valid_parentheses("(())((()())())"))       #True
# print(valid_parentheses("hi(hi)()"))             #True
# print(valid_parentheses(")test"))
# print(valid_parentheses(""))
print(valid_parentheses('w(zh)rlerot)wms(xx(i)qemzl)xjiffbft((u)'))    #False