def valid_parentheses(string):
    stack = []
    stackN = []
    parentheses = ['(', ')']
    parenthesisList = []



    for item in string:
        if item in parentheses:
            parenthesisList += item

    # print('pL', parenthesisList)


    if parenthesisList == []:
        return True

    elif parenthesisList[0] == ')' or parenthesisList[-1] == '(':
        return False

    else:
        for i in parenthesisList:
            if i == '(':
                stack.append('(')
                # print('st(', stack)
            elif i == ')':
                try:
                    stack.remove('(')
                    # print('st)', stack)
                except ValueError:
                    pass

        for j in range(len(parenthesisList)-1, 0 - 1, -1):
            # print('j', j)
            if parenthesisList[j] == ')':
                stackN.append(')')
                # print('stN)', stackN)
            elif parenthesisList[j] == '(':
                try:
                    stackN.remove(')')
                    # print('stN)', stackN)
                except ValueError:
                    pass

        # print('st()', stack)
        # print('stN()', stackN)
        if stack or stackN:
            return False
        else:
            return True



# print(valid_parentheses("()"))                   #True
# print(valid_parentheses(")(()))"))               #False
# print(valid_parentheses("("))                    #False
# print(valid_parentheses("(())((()())())"))       #True
# print(valid_parentheses("hi(hi)()"))             #True
# print(valid_parentheses(")test"))
# print(valid_parentheses(""))
# print(valid_parentheses('w(zh)rlerot)wms(xx(i)qemzl)xjiffbft((u)'))    #False
print(valid_parentheses('jvq(uxbvimcrjeiu(jmg)nynl)vmw)rfhip'))