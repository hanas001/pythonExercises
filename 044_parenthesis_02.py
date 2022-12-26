def valid_parentheses(string):
    stack = 0
    for item in string:
        if item == '(':
            stack += 1
            # print('st+', stack)
        elif item == ')' and stack > 0:
            stack -= 1
            # print('st-', stack)
    # print(stack)
    if stack == 0:
        return True
    else:
        return False



# print(valid_parentheses("()"))                   #True
# print(valid_parentheses(")(()))"))               #False
# print(valid_parentheses("("))                    #False
# print(valid_parentheses("(())((()())())"))       #True
# print(valid_parentheses("hi(hi)()"))             #True
# print(valid_parentheses('hi())('))                #False
print(valid_parentheses(")test"))
# print(valid_parentheses(""))
# print(valid_parentheses('w(zh)rlerot)wms(xx(i)qemzl)xjiffbft((u)'))    #False
# print(valid_parentheses('jvq(uxbvimcrjeiu(jmg)nynl)vmw)rfhip'))